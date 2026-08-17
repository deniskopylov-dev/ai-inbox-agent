from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db import Base, engine
from app.routers import tickets


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        Base.metadata.create_all(bind=engine)
    except Exception:
        # No DB reachable at import time (e.g. running under pytest without
        # docker-compose). Tests create their own schema against an
        # in-memory sqlite engine in tests/conftest.py.
        pass
    yield


app = FastAPI(
    title="AI Inbox & Ticket Automation Agent",
    description="Classifies, prioritizes and drafts replies to support tickets using an LLM + RAG pipeline.",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(tickets.router)


@app.get("/health")
def health():
    return {"status": "ok"}
