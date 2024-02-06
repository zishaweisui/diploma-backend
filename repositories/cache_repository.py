class CacheRepository:
    def __init__(self, redis, lifetime):
        self.redis = redis
        self.default_ttl: int = lifetime

    def get_booked(self, key: str) -> list[str]:
        return self.redis.keys(f"*:{key}")

    def book(self, key, ttl=None) -> None:
        ttl = ttl or self.default_ttl
        self.redis.setex(key, ttl, 1)

    def unbook(self, key: str) -> None:
        self.redis.delete(key)

    def get_all(self):
        return self.redis.keys("*")
