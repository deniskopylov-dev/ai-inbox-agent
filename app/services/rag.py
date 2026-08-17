"""
Retrieval layer — currently a stub returning no context.

Milestone 3 (see ROADMAP.md) replaces this with a real pgvector-backed
similarity search over an ingested knowledge base. Kept as its own module
now so `draft_generator.py` never needs to change when that lands.
"""


def retrieve_context(query: str, top_k: int = 3) -> list[str]:
    return []
