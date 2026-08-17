# AI Inbox & Ticket Automation Agent

![CI](https://github.com/deniskopylov-dev/ai-inbox-agent/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.12-blue.svg)

Classifies, prioritizes and drafts replies to incoming support tickets / emails using an LLM, with a lightweight RAG layer over a knowledge base of past answers and docs.

Built as a portfolio piece aimed at a real, sellable use case: small/medium businesses that get more support requests than they can triage by hand. This is the first public project in an ongoing plan to move into international remote/freelance work — see the "Roadmap" section below for where this fits.

## Why this project

Support/ticket triage is one of the most common paid AI-automation asks from small businesses internationally (Upwork, Web3 support desks, e-commerce). It's a great portfolio piece because it demonstrates, in one project:

- a real backend (FastAPI + PostgreSQL + Docker) — not just a notebook
- LLM integration done properly (structured output, RAG grounding, cost/latency awareness)
- tests and CI, not just a script that ran once on your machine

## Architecture

```
Incoming ticket (API / webhook)
        │
        ▼
 [Classifier]  ── LLM structured output → category, priority, sentiment
        │
        ▼
 [RAG retriever] ── pgvector similarity search over knowledge base
        │
        ▼
 [Draft generator] ── LLM + retrieved context → draft reply
        │
        ▼
   Stored ticket + draft, exposed via REST API
```

## Stack

- **FastAPI** — REST API
- **PostgreSQL** (+ `pgvector` extension) — ticket storage and embeddings
- **SQLAlchemy** — ORM
- **Docker / docker-compose** — local dev environment
- **pytest** — tests
- **GitHub Actions** — CI (lint + tests on every push)
- LLM provider is abstracted behind `app/services/llm_client.py` — swap in OpenAI, Anthropic, or a local model without touching business logic.

## Status

This repo is being built in public, incrementally. Current milestone: core API + data model + mocked LLM pipeline (deterministic, so tests are reproducible without API keys). Next milestones are tracked in `ROADMAP.md`.

## Getting started

```bash
cp .env.example .env
docker compose up --build
```

API docs available at `http://localhost:8000/docs` once running.

Run tests:

```bash
docker compose run --rm app pytest
```

## Project layout

```
app/
  main.py            # FastAPI app entrypoint
  config.py          # settings via pydantic-settings
  db.py              # SQLAlchemy engine/session
  models.py          # ORM models
  schemas.py         # Pydantic request/response schemas
  services/
    llm_client.py     # LLM provider abstraction (mocked by default)
    classifier.py      # ticket classification logic
    rag.py              # retrieval over knowledge base
    draft_generator.py  # reply drafting
  routers/
    tickets.py         # /tickets endpoints
tests/
  test_tickets.py
```

## Roadmap for this repo

- [ ] Wire a real LLM provider behind `llm_client.py` (OpenAI-compatible, with a local fallback)
- [ ] Add `pgvector`-based retrieval with real embeddings
- [ ] Add a minimal web UI to review/approve drafted replies
- [ ] Add usage-based cost tracking per ticket (token accounting)
- [ ] Deploy a live demo

---

**Author:** Denis Kopylov — [github.com/deniskopylov-dev](https://github.com/deniskopylov-dev) · denis@kopylov1.ru
