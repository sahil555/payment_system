from fastapi import APIRouter, Depends
from app.schemas.payment import PaymentRequest
from app.services.payment_service import PaymentService
from app.services.ledger_service import LedgerService
from app.services.idempotency_service import IdempotencyService
from app.dependencies import KafkaProducer
from app.db.session import get_db

router = APIRouter()

@router.post("/payments")
async def create_payment(payload: PaymentRequest, db=Depends(get_db)):

    service = PaymentService(
        LedgerService(),
        IdempotencyService(),
        KafkaProducer()
    )

    result = await service.process_payment(db, payload)
    return result