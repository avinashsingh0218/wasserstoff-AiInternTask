import aioredis
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost")

class RedisCache:
    def __init__(self):
        self.redis = None

    async def connect(self):
        self.redis = await aioredis.from_url(REDIS_URL)

    async def close(self):
        if self.redis:
            await self.redis.close()

    async def get_verdict(self, key: str):
        return await self.redis.get(key)

    async def set_verdict(self, key: str, value: str, expire: int = 3600):
        await self.redis.set(key, value, ex=expire)
from backend.core.cache import RedisCache

cache = RedisCache()

# Connect on app start
@app.on_event("startup")
async def startup_event():
    await cache.connect()

# Disconnect on shutdown
@app.on_event("shutdown")
async def shutdown_event():
    await cache.close()
