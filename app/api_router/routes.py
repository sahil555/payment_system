from fastapi import APIRouter, Depends
from app.schemas.payment import PaymentRequest
from app.services.payment_service import PaymentService
from app.services.ledger_service import LedgerService
from app.services.idempotency_service import IdempotencyService
from payment_system.app.dependencies.auth import get_current_user
from payment_system.app.dependencies.kafkaProducer import KafkaProducer
from app.db.session import get_db

router = APIRouter()

@router.post("/payments")
async def create_payment(
    payload: PaymentRequest, 
    db=Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    
    print(f"Processing payment for user: {user_id}")

    service = PaymentService(
        LedgerService(),
        IdempotencyService(),
        KafkaProducer()
    )

    result = await service.process_payment(db, payload)
    return result