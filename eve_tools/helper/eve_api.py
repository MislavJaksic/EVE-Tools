from eve_tools import settings

from eve_tools.helper.file_cache import FileCache
from eve_tools.helper.swaggerer import Swaggerer


class EveApi:
    def __init__(self, swagger_uri, cache_path):
        self.swaggerer = Swaggerer(swagger_uri)
        self.cache = FileCache(cache_path)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.cache.close()

    def get_data_from(self, get_operation_id, **parameters):
        key = self.create_key(get_operation_id, **parameters)
        if self.cache.exists(key):
            response = self.cache.get(key)
        else:
            response = self.swaggerer.do(key)
            self.cache.set(key, response)
        return response.data

    def create_key(self, get_operation_id, **parameters):
        return (get_operation_id, sorted(parameters.items(), key=lambda kv: kv[0]))


with EveApi(settings.swagger_uri, settings.cache_path) as api:
    npc_corp_ids = api.get_data_from("get_corporations_npccorps")
    print(npc_corp_ids)
    for npc_corp_id in npc_corp_ids:
        print(npc_corp_id)
        print(
            api.get_data_from(
                "get_corporations_corporation_id", corporation_id=npc_corp_id
            )
        )
