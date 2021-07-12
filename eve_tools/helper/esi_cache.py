from rapdevpy.file_cache import FileCache

from eve_tools import settings


class EsiCache:
    """
    Check cache if ESI data exists
    If YES, send ETag to ESI and check response
        If YES, overwrite cache
        If NO, get data from cache
    If NO
        Get data from ESI
        Cache data from ESI
        Present data
    """
    def __init__(self):
        self.cache = FileCache(settings.cache_path)