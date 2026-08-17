from app.services.llm_client import get_llm_client
from app.services.rag import retrieve_context


def generate_draft(subject: str, body: str) -> str:
    client = get_llm_client()
    context = retrieve_context(query=f"{subject} {body}")
    return client.draft_reply(subject, body, context)
