# Roadmap

Tracked separately from the main README so progress is easy to see at a glance.

## Milestone 1 — Core skeleton (done in this scaffold)
- [x] FastAPI app with `/tickets` CRUD
- [x] SQLAlchemy models + PostgreSQL via docker-compose
- [x] Mocked LLM classification + draft generation (deterministic, no API key required)
- [x] Pytest suite covering the API
- [x] GitHub Actions CI

## Milestone 2 — Real LLM integration
- [ ] Implement `llm_client.py` against a real provider (OpenAI-compatible API)
- [ ] Structured output (function calling / JSON schema) for classification
- [ ] Prompt + eval harness: a small labeled set of example tickets to check classification accuracy before/after prompt changes

## Milestone 3 — Retrieval (RAG)
- [ ] Add `pgvector` extension + embeddings table
- [ ] Ingest a small knowledge base (FAQ / docs) as the grounding source
- [ ] Retrieval-augmented draft generation, with citations back to source docs

## Milestone 4 — Product polish
- [ ] Minimal review UI (approve/edit/reject drafts) — even a simple server-rendered page is enough
- [ ] Webhook ingestion (e.g. from email or a helpdesk tool) instead of manual POST
- [ ] Token/cost accounting per ticket, logged and queryable

## Milestone 5 — Ship it as a demo
- [ ] Deploy (Railway/Fly.io/Render — pick whichever has an easy free tier)
- [ ] Record a 60-90s demo video/gif for the README and portfolio site
- [ ] Write a short case-study writeup: problem, approach, tradeoffs, what you'd do differently

This maps to the "Building now" / "Coming soon" cards on the portfolio site — update those once a milestone ships.
