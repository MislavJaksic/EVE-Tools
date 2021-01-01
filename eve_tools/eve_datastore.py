from eve_tools.helper.swagger_api import SwaggerApi

from eve_tools import settings


class EveDatastore:
    def __init__(self):
        self.api = SwaggerApi(settings.swagger_uri, settings.cache_path)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def get_npc_corporations(self):
        list = []
        npc_corp_ids = self.api.get_json_from("get_corporations_npccorps")
        for npc_corp_id in npc_corp_ids:
            list.append(
                self.api.get_json_from(
                    "get_corporations_corporation_id", corporation_id=npc_corp_id
                )
            )
        return list

    def get_loyalty_point_offers(self):
        list = []
        npc_corp_ids = self.api.get_json_from("get_corporations_npccorps")
        for npc_corp_id in npc_corp_ids:
            data = self.api.get_json_from(
                "get_loyalty_stores_corporation_id_offers", corporation_id=npc_corp_id
            )
            list.extend(data)
        return list

    def close(self):
        self.api.close()
