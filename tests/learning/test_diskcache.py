from tests import context

import pytest
from diskcache import Cache

from tests import settings

# Learner's tests


@pytest.fixture(scope="function")
def cache():
    cache = Cache(settings.test_cache_path)
    cache.set("key", "value", expire=60, read=False, tag="data")
    yield cache
    del cache["key"]
    cache.close()


class TestEternalCache:
    def test_get_good(self, cache):
        assert cache["key"] == "value"

    def test_get_bad(self, cache):
        with pytest.raises(KeyError):
            cache["bad"]
