import enum
from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, Enum
from app.db import Base


class Priority(str, enum.Enum):
    low = "low"
    normal = "normal"
    high = "high"
    urgent = "urgent"


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String, nullable=False)
    body = Column(Text, nullable=False)
    sender = Column(String, nullable=True)

    category = Column(String, nullable=True)
    priority = Column(Enum(Priority), nullable=True)
    sentiment = Column(String, nullable=True)
    draft_reply = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
