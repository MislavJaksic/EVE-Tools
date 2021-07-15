from datetime import timedelta
from typing import Callable

from loguru import logger
from rapdevpy.file_cache import FileCache

from eve_tools import settings
from eve_tools.swagger_client.api.universe_api import UniverseApi
from eve_tools.swagger_client.rest import ApiException

log_message = "what={object}, why={reason}, how={action}"


class EveDatastore:
    def __init__(self):
        self.cache = FileCache(settings.cache_path)

        self.universe_api = UniverseApi()

    def get_data(self, api_function: Callable, expire_timedelta: timedelta):
        api_name = api_function.__name__
        if self.cache.is_exists(api_name):
            response = self.get_and_check_etag(api_function, expire_timedelta)
        else:
            response = self.get_and_cache(api_function, expire_timedelta)
        logger.info(log_message, object=str(response["status"]) + ", " + str(self.extract_etag(response)), reason="Inspection", action="Get data")

        return response["data"]

    def get_and_check_etag(self, api_function: Callable, expire_timedelta: timedelta):
        api_name = api_function.__name__
        logger.info(log_message, object=api_name, reason="Cache hit", action="Access cache")
        response = self.cache.get(api_name)
        etag = self.extract_etag(response)
        try:
            response = api_function(if_none_match=etag)
            self.cache.set(api_name, response, expire_timedelta)
            logger.info(log_message, object=api_name + ", " + etag, reason="ETag expired", action="Etag check")
        except ApiException as e:
            print("Status: {}".format(e.status))
            print("Reason: {}".format(e.reason))
            print("Body: {}".format(e.body))
            print("Headers: {}".format(e.headers))

        return response

    def extract_etag(self, response: dict):
        return response["headers"]["ETag"].split('"')[1]

    def get_and_cache(self, api_function: Callable, expire_timedelta: timedelta):
        api_name = api_function.__name__
        logger.info(log_message, object=api_name, reason="Cache miss", action="Access cache")
        response = api_function()
        self.cache.set(api_name, response, expire_timedelta)
        return response

    def get_universe_system_kills(self):
        systems = self.get_data(self.universe_api.get_universe_systems, timedelta(days=30))

        empty_kills = []
        for system in systems:
            empty = {"npc_kills": 0, "pod_kills": 0, "ship_kills": 0, "system_id": system}
            empty_kills.append(empty)

        system_kills = self.get_data(self.universe_api.get_universe_system_kills, timedelta(hours=1))
        for system_kill in system_kills:
            for empty_kill in empty_kills:
                if empty_kill["system_id"] == system_kill["system_id"]:
                    empty_kill["npc_kills"] = system_kill["npc_kills"]
                    empty_kill["pod_kills"] = system_kill["pod_kills"]
                    empty_kill["ship_kills"] = system_kill["ship_kills"]

        return empty_kills


