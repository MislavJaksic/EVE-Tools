import requests
from cachecontrol import CacheControl
from cachecontrol.caches import FileCache
from cachecontrol.heuristics import ExpiresAfter
from eve_tools.settings import settings


class Requester:
    def __init__(self, max_age_days):
        session = requests.Session()
        expiration = ExpiresAfter(days=max_age_days)
        cache = FileCache(settings.cache_path)
        self.control = CacheControl(session, heuristic=expiration, cache=cache)

    def get_json(self, uri):
        return self.control.get(uri).json()
