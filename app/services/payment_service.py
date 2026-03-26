from app.models.payment import Payment, PaymentStatus

class PaymentService:

    def __init__(self, ledger, idempotency, kafka):
        self.ledger = ledger
        self.idempotency = idempotency
        self.kafka = kafka

    async def process_payment(self, db, payload):

        # 1. Idempotency
        existing = await self.idempotency.get(payload.idempotency_key)
        if existing:
            return {"status": "duplicate"}

        # 2. Create Payment
        payment = Payment(
            amount=payload.amount,
            user_id=payload.user_id,
            merchant_id=payload.merchant_id,
            status=PaymentStatus.PROCESSING,
            idempotency_key=payload.idempotency_key
        )

        db.add(payment)
        await db.flush()

        # 3. Ledger
        await self.ledger.create_entries(db, payment)

        # 4. Simulated gateway
        payment.status = PaymentStatus.SUCCESS

        await db.commit()

        # 5. Idempotency store
        await self.idempotency.set(
            payload.idempotency_key,
            payment.id
        )

        # 6. Kafka event
        await self.kafka.send(
            "payments",
            {"payment_id": payment.id, "status": payment.status}
        )

        return payment