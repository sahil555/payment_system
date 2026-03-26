from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@db:5432/payments"
    REDIS_URL: str = "redis://redis:6379"
    KAFKA_BOOTSTRAP_SERVERS: str = "kafka:9094"

settings = Settings()