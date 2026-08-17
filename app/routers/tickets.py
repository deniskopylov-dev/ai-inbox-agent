from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Ticket
from app.schemas import TicketCreate, TicketOut
from app.services.classifier import classify_ticket
from app.services.draft_generator import generate_draft

router = APIRouter(prefix="/tickets", tags=["tickets"])


@router.post("", response_model=TicketOut, status_code=201)
def create_ticket(payload: TicketCreate, db: Session = Depends(get_db)):
    classification = classify_ticket(payload.subject, payload.body)
    draft = generate_draft(payload.subject, payload.body)

    ticket = Ticket(
        subject=payload.subject,
        body=payload.body,
        sender=payload.sender,
        category=classification["category"],
        priority=classification["priority"],
        sentiment=classification["sentiment"],
        draft_reply=draft,
    )
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket


@router.get("", response_model=list[TicketOut])
def list_tickets(db: Session = Depends(get_db)):
    return db.query(Ticket).order_by(Ticket.created_at.desc()).all()


@router.get("/{ticket_id}", response_model=TicketOut)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket
