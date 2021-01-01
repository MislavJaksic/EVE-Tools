from diskcache import Cache
import hashlib
import pickle

from eve_tools import settings


class FileCache:
    def __init__(self, cache_path):
        self.cache_path = cache_path
        self.cache = Cache(self.cache_path)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def exists(self, key):
        key_hash = self.hash(key)
        return key_hash in self.cache

    def get(self, key):
        key_hash = self.hash(key)
        return self.cache[key_hash]

    def set(self, key, value, expire_seconds=None):
        key_hash = self.hash(key)
        self.cache.set(key_hash, value, expire=expire_seconds)

    def delete(self, key):
        key_hash = self.hash(key)
        del self.cache[key_hash]

    def hash(self, data):
        return hashlib.sha512(pickle.dumps(data)).hexdigest()

    def close(self):
        self.cache.close()
