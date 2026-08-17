from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://postgres:postgres@localhost:5432/inbox_agent"
    llm_provider: str = "mock"
    openai_api_key: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()
