import redis.asyncio as redis
from app.core.config import settings

class IdempotencyService:
    def __init__(self):
        self.client = redis.from_url(settings.REDIS_URL)

    async def get(self, key):
        return await self.client.get(key)

    async def set(self, key, value):
        await self.client.set(key, value, ex=86400)