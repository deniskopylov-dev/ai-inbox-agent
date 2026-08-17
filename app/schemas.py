from datetime import datetime
from pydantic import BaseModel


class TicketCreate(BaseModel):
    subject: str
    body: str
    sender: str | None = None


class TicketOut(BaseModel):
    id: int
    subject: str
    body: str
    sender: str | None
    category: str | None
    priority: str | None
    sentiment: str | None
    draft_reply: str | None
    created_at: datetime

    class Config:
        from_attributes = True
