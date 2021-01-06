import hashlib
from datetime import timedelta
from diskcache import Cache


class FileCache:
    def __init__(self, cache_path):
        self.cache_path = cache_path
        self.cache = Cache(self.cache_path)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def exists(self, key):
        digest = self.digest(key)
        return digest in self.cache

    def get(self, key):
        digest = self.digest(key)
        return self.cache[digest]

    def set(self, key, value, expire_timedelta=timedelta(days=7)):
        digest = self.digest(key)
        seconds = self.total_seconds(expire_timedelta)
        self.cache.set(digest, value, expire=seconds)

    def touch(self, key, expire_timedelta):
        digest = self.digest(key)
        seconds = self.total_seconds(expire_timedelta)
        self.cache.touch(digest, expire=seconds)

    def delete(self, key):
        digest = self.digest(key)
        del self.cache[digest]

    def digest(self, data):
        return hashlib.sha512(str(data).encode()).hexdigest()

    def total_seconds(self, time_delta):
        return int(time_delta.total_seconds())

    def clear(self):
        self.cache.clear()

    def close(self):
        self.cache.close()
