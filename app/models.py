from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class WalletRequest(Base):
    __tablename__ = "wallet_requests"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
    bandwidth = Column(Integer)
    energy = Column(Integer)
    balance = Column(String)
    timestamp = Column(DateTime, default=lambda: datetime.now())
