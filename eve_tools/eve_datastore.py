from datetime import timedelta

from eve_tools.helper.swagger_api import SwaggerApi
from eve_tools.eve_contract import EveItemExchange

from eve_tools import settings


class EveDatastore:
    def __init__(self):
        self.api = SwaggerApi(settings.swagger_uri, settings.cache_path)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def get_alliance_ids(self):
        return self.get_json("get_alliances")

    def get_alliances(self):
        list = []
        ids = self.get_alliance_ids()
        for id in ids:
            list.append(self.get_json("get_alliances_alliance_id", alliance_id=id))
        return list

    def get_alliance_corporations(self, id):
        list = []
        ids = self.get_json_ids(
            "get_alliances_alliance_id_corporations", alliance_id=id
        )
        for id in ids:
            list.append(
                self.get_json("get_corporations_corporation_id", corporation_id=id)
            )
        return list

    def get_region_contracts(self, id):
        return self.get_json_paged(
            "get_contracts_public_region_id",
            region_id=id,
            expire_timedelta=timedelta(hours=12),
        )

    def get_region_item_exchanges(self, id):
        contracts = self.get_region_contracts(id)
        list = []
        for contract in contracts:
            try:
                if contract["type"] == "item_exchange":
                    contract_id = contract["contract_id"]
                    items = self.get_json_paged(
                        "get_contracts_public_items_contract_id",
                        contract_id=contract_id,
                        expire_timedelta=timedelta(hours=12),
                    )
                    exchange = EveItemExchange(contract, items)
                    print(exchange)
                    list.append(exchange)
            except:
                print("Contract expired")
        return list

    def get_npc_corporations(self):
        list = []
        ids = self.get_json_ids("get_corporations_npccorps")
        for id in ids:
            list.append(
                self.get_json("get_corporations_corporation_id", corporation_id=id)
            )
        return list

    def get_loyalty_point_offers(self):
        list = []
        ids = self.get_json_ids("get_corporations_npccorps")
        for id in ids:
            data = self.get_json(
                "get_loyalty_stores_corporation_id_offers", corporation_id=id
            )
            list.extend(data)
        return list

    def get_factions(self):
        return self.get_json("get_universe_factions", language="en-us")

    def get_region_ids(self):
        return self.get_json("get_universe_regions")

    def get_regions(self):
        list = []
        ids = self.get_region_ids()
        for id in ids:
            data = self.get_json(
                "get_universe_regions_region_id", region_id=id, language="en-us"
            )
            list.append(data)
        return list

    def get_json_paged(self, operation_id, **parameters):
        max_page = self.get_max_page(operation_id, **parameters)
        page = 1
        list = []
        if max_page >= page:
            data = self.get_json(
                operation_id,
                page=page,
                **parameters,
            )
            list.extend(data)
            page += 1
        return list

    def get_json(self, operation_id, **parameters):
        return self.api.get_response_from(operation_id, **parameters).json

    def get_max_page(self, operation_id, **parameters):
        response = self.api.get_response_from(operation_id, page=1, **parameters)
        return response.header["x-pages"][0]

    def close(self):
        self.api.close()
