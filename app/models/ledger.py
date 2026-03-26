from sqlalchemy import Column, String, Integer
from app.models.payment import Base

class LedgerEntry(Base):
    __tablename__ = "ledger_entries"

    id = Column(String, primary_key=True)
    account_id = Column(String)
    amount = Column(Integer)
    type = Column(String)
    payment_id = Column(String)