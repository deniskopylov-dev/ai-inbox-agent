from app.services.llm_client import get_llm_client


def classify_ticket(subject: str, body: str) -> dict:
    client = get_llm_client()
    return client.classify(subject, body)
