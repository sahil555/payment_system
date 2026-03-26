from pydantic import BaseModel

class PaymentRequest(BaseModel):
    amount: int
    user_id: str
    merchant_id: str
    idempotency_key: str