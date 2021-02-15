from tests import context

import pytest
from eve_tools.helper.file_cache import FileCache

from tests import settings


# @pytest.fixture(scope="function")
# def cache():
#     with FileCache(settings.test_cache_path) as cache:
#         cache.set("key", "value", expire_seconds=60)
#         cache.set("dict_of_dict", {"Alice": {"Bob": 1}}, expire_seconds=60)
#         yield cache
#         cache.clear()
#
#
# class TestSet:
#     def test_string(self, cache):
#         pass


# class TestCache:
#     def test_get_good(self, cache):
#         assert cache["key"] == "value"
#
#     def test_get_bad(self, cache):
#         with pytest.raises(KeyError):
#             cache["bad"]
#
#     def __init__(self, cache_path):
#         self.cache_path = cache_path
#         self.cache = Cache(self.cache_path)
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         self.close()
#
#     def exists(self, key):
#         digest = self.digest(key)
#         return digest in self.cache
#
#     def get(self, key):
#         digest = self.digest(key)
#         return self.cache[digest]
#
#     def set(self, key, value, expire_seconds=None):
#         digest = self.digest(key)
#         self.cache.set(digest, value, expire=expire_seconds)
#
#     def delete(self, key):
#         digest = self.digest(key)
#         del self.cache[digest]
#
#     def digest(self, data):
#         return hashlib.sha512(str(data).encode()).hexdigest()
#
#     def close(self):
#         self.cache.close()
