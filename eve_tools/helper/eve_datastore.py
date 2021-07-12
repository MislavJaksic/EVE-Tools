from rapdevpy.file_cache import FileCache

from eve_tools import settings
from eve_tools.helper.esi_cache import EsiCache
from eve_tools.swagger_client.api.universe_api import UniverseApi


class EveDatastore:
    def __init__(self):
        self.cache = FileCache(settings.cache_path)

        self.universe_api = UniverseApi()

    def get_universe_system_kills(self):
        self.cache.get("get_universe_systems")
        systems, status, headers = self.universe_api.get_universe_systems(if_none_match=if_none_match)

        empty_kills = []
        for system in systems:
            empty = {"npc_kills": 0, "pod_kills": 0, "ship_kills": 0, "system_id": system}
            empty_kills.append(empty)

        system_kills, status, headers = self.universe_api.get_universe_system_kills()
        for system_kill in system_kills:
            for empty_kill in empty_kills:
                if empty_kill["system_id"] == system_kill["system_id"]:
                    empty_kill["npc_kills"] = system_kill["npc_kills"]
                    empty_kill["pod_kills"] = system_kill["pod_kills"]
                    empty_kill["ship_kills"] = system_kill["ship_kills"]

        return empty_kills

    # api_instance = swagger_client.UniverseApi()
    # if_none_match = 'ba0a7521d5744c38efbfebd928e48724b11f27e6f77dcdf483d5909c'  # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    #
    # try:
    #     # Get system kills
    #     response = api_instance.get_universe_system_kills(if_none_match=if_none_match)
    #     print(response["data"])
    #     print(response["status"])
    #     print(response["headers"])
    # except ApiException as e:
    #     print("Status: {}".format(e.status))
    #     print("Reason: {}".format(e.reason))
    #     print("Body: {}".format(e.body))
    #     print("Headers: {}".format(e.headers))
