from sqlalchemy import Column, String, Integer, Enum
from sqlalchemy.ext.declarative import declarative_base
import enum
import uuid

Base = declarative_base()

class PaymentStatus(str, enum.Enum):
    INITIATED = "INITIATED"
    PROCESSING = "PROCESSING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    PENDING = "PENDING"

class Payment(Base):
    __tablename__ = "payments"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    amount = Column(Integer)
    user_id = Column(String)
    merchant_id = Column(String)
    status = Column(Enum(PaymentStatus))
    idempotency_key = Column(String, unique=True)