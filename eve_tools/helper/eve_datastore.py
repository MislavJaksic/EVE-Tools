from datetime import timedelta
from typing import Callable

from loguru import logger
from rapdevpy.file_cache import FileCache

from eve_tools import settings
from eve_tools.swagger_client import ContractsApi
from eve_tools.swagger_client.api.universe_api import UniverseApi
from eve_tools.swagger_client.rest import ApiException

log_message = "what={object}, why={reason}, how={action}"


class EveDatastore:
    def __init__(self):
        self.cache = FileCache(settings.cache_path)

        self.universe_api = UniverseApi()
        self.contract_api = ContractsApi()

    def get_data(self, api_function: Callable, expire_timedelta: timedelta, *args, **kwargs):
        return self.get_response(api_function, expire_timedelta, *args, **kwargs)["data"]

    def get_response(self, api_function: Callable, expire_timedelta: timedelta, *args, **kwargs):
        key = (api_function.__name__, *args, **kwargs)
        if self.cache.is_exists(key):
            response = self.get_and_check_etag(api_function, expire_timedelta, *args, **kwargs)
        else:
            response = self.get_and_cache(api_function, expire_timedelta, *args, **kwargs)
        logger.info(log_message, object=str(response["status"]) + ", " + str(self.extract_etag(response)),
                    reason="Inspection", action="Get data")

        return response

    def get_and_check_etag(self, api_function: Callable, expire_timedelta: timedelta, *args, **kwargs):
        api_name = api_function.__name__
        logger.info(log_message, object=api_name + ", " + str(*args) + ", " + str(**kwargs), reason="Cache hit", action="Access cache")
        response = self.cache.get(api_name)
        etag = self.extract_etag(response)
        try:
            response = api_function(if_none_match=etag, **kwargs)
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

    def get_and_cache(self, api_function: Callable, expire_timedelta: timedelta, *args, **kwargs):
        api_name = api_function.__name__
        logger.info(log_message, object=api_name + ", " + str(*args) + ", " + str(**kwargs), reason="Cache miss", action="Access cache")
        response = api_function(**kwargs)
        self.cache.set(api_name, response, expire_timedelta)
        return response

    def get_universe_system_kills(self):
        systems = self.get_response(self.universe_api.get_universe_systems, timedelta(days=30))

        empty_kills = []
        for system in systems:
            empty = {"npc_kills": 0, "pod_kills": 0, "ship_kills": 0, "system_id": system}
            empty_kills.append(empty)

        system_kills = self.get_response(self.universe_api.get_universe_system_kills, timedelta(hours=1))
        for system_kill in system_kills:
            for empty_kill in empty_kills:
                if empty_kill["system_id"] == system_kill["system_id"]:
                    empty_kill["npc_kills"] = system_kill["npc_kills"]
                    empty_kill["pod_kills"] = system_kill["pod_kills"]
                    empty_kill["ship_kills"] = system_kill["ship_kills"]

        return empty_kills

    def get_universe_regions(self):
        return self.get_data(self.universe_api.get_universe_regions, timedelta(days=30))

    def get_contracts_public_region_id(self, region_id: int):
        response = self.get_response(self.contract_api.get_contracts_public_region_id, timedelta(minutes=30), region_id)

        for page in pages:
            self.get_data(self.contract_api.get_contracts_public_region_id, timedelta(minutes=30), region_id, page=page)

















