"""
LLM provider abstraction.

Everything else in this codebase talks to `LLMClient`, never to a specific
provider SDK directly. That means swapping OpenAI <-> Anthropic <-> a local
model later is a one-file change, not a rewrite.

`MockLLMClient` is deterministic on purpose: it lets classifier/draft tests
run in CI without an API key and without network calls. Milestone 2 in
ROADMAP.md is wiring a real provider behind the same interface.
"""

from abc import ABC, abstractmethod

from app.config import settings


class LLMClient(ABC):
    @abstractmethod
    def classify(self, subject: str, body: str) -> dict:
        """Return {category, priority, sentiment}."""
        raise NotImplementedError

    @abstractmethod
    def draft_reply(self, subject: str, body: str, context: list[str]) -> str:
        """Return a drafted reply string, grounded in `context` (RAG chunks)."""
        raise NotImplementedError


class MockLLMClient(LLMClient):
    URGENT_KEYWORDS = {"urgent", "asap", "down", "outage", "broken", "critical"}
    NEGATIVE_KEYWORDS = {"angry", "refund", "cancel", "terrible", "worst", "disappointed"}

    def classify(self, subject: str, body: str) -> dict:
        text = f"{subject} {body}".lower()

        priority = "urgent" if any(k in text for k in self.URGENT_KEYWORDS) else "normal"
        sentiment = "negative" if any(k in text for k in self.NEGATIVE_KEYWORDS) else "neutral"

        if "billing" in text or "invoice" in text or "payment" in text:
            category = "billing"
        elif "bug" in text or "error" in text or "broken" in text:
            category = "technical"
        else:
            category = "general"

        return {"category": category, "priority": priority, "sentiment": sentiment}

    def draft_reply(self, subject: str, body: str, context: list[str]) -> str:
        grounding = f" Referencing: {'; '.join(context)}." if context else ""
        return (
            f"Hi, thanks for reaching out about \"{subject}\". "
            f"We've received your message and are looking into it.{grounding} "
            f"We'll follow up shortly. — Support"
        )


def get_llm_client() -> LLMClient:
    if settings.llm_provider == "mock":
        return MockLLMClient()
    # Milestone 2: add real providers here, e.g.
    # if settings.llm_provider == "openai": return OpenAILLMClient()
    raise ValueError(f"Unknown LLM_PROVIDER: {settings.llm_provider}")
