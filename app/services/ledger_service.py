from app.models.ledger import LedgerEntry
import uuid

class LedgerService:
    async def create_entries(self, db, payment):
        debit = LedgerEntry(
            id=str(uuid.uuid4()),
            account_id=payment.user_id,
            amount=payment.amount,
            type="DEBIT",
            payment_id=payment.id
        )

        credit = LedgerEntry(
            id=str(uuid.uuid4()),
            account_id=payment.merchant_id,
            amount=payment.amount,
            type="CREDIT",
            payment_id=payment.id
        )

        db.add_all([debit, credit])