from redis.asyncio import Redis as AioRedis
from redis.asyncio import from_url
from settings import REDIS_CONNECTION_STRING
from asyncio import wait_for

class Redis:
    _client: AioRedis | None = None

    @classmethod
    async def _connect(cls):
        if not cls._client:
            cls._client = await from_url(REDIS_CONNECTION_STRING)

    @classmethod
    async def close(cls):
        if cls._client is not None:
            await wait_for(cls._client.close())
            cls._client = None

    @classmethod
    async def get_client(cls) -> AioRedis:
        if not cls._client:
            await cls._connect()
        return cls._client
