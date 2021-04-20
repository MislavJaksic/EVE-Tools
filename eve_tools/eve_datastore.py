from datetime import timedelta

from eve_tools import settings

from eve_tools.swagger_client.api.universe_api import UniverseApi


class EveDatastore:
    def __init__(self):
        self.universe_api = UniverseApi()

    # def get_alliance_ids(self):
    #     return self.get_json("get_alliances")
    #
    # def get_alliances(self):
    #     list = []
    #     ids = self.get_alliance_ids()
    #     for id in ids:
    #         list.append(self.get_json("get_alliances_alliance_id", alliance_id=id))
    #     return list
    #
    # def get_alliance_corporations(self, id):
    #     list = []
    #     ids = self.get_json_ids(
    #         "get_alliances_alliance_id_corporations", alliance_id=id
    #     )
    #     for id in ids:
    #         list.append(
    #             self.get_json("get_corporations_corporation_id", corporation_id=id)
    #         )
    #     return list
    #
    # def get_region_contracts(self, id):
    #     return self.get_json_paged(
    #         "get_contracts_public_region_id",
    #         region_id=id,
    #         expire_timedelta=timedelta(hours=12),
    #     )
    #
    # def get_region_item_exchanges(self, id):
    #     contracts = self.get_region_contracts(id)
    #     types = self.get_types_dict()
    #     list = []
    #     for contract in contracts:
    #         if contract["type"] == "item_exchange":
    #             contract_id = contract["contract_id"]
    #             items = self.get_json_paged(
    #                 "get_contracts_public_items_contract_id",
    #                 contract_id=contract_id,
    #                 expire_timedelta=timedelta(hours=12),
    #             )
    #
    #             for item in items:
    #                 item["type"] = types[item["type_id"]]
    #
    #             exchange = EveItemExchange(contract, items)
    #             list.append(exchange)
    #     return list
    #
    # def get_region_item_exchange_blueprints(self, id):
    #     contracts = self.get_region_item_exchanges(id)
    #     list = []
    #     for contract in contracts:
    #         for item in contract.items:
    #             if "Blueprint" in item["type"]["name"]:
    #                 list.append(contract)
    #     return list
    #
    # def get_npc_corporations(self):
    #     list = []
    #     ids = self.get_json_ids("get_corporations_npccorps")
    #     for id in ids:
    #         list.append(
    #             self.get_json("get_corporations_corporation_id", corporation_id=id)
    #         )
    #     return list
    #
    # def get_loyalty_point_offers(self):
    #     list = []
    #     ids = self.get_json_ids("get_corporations_npccorps")
    #     for id in ids:
    #         data = self.get_json(
    #             "get_loyalty_stores_corporation_id_offers", corporation_id=id
    #         )
    #         list.extend(data)
    #     return list
    #
    # def get_factions(self):
    #     return self.get_json("get_universe_factions", language="en-us")
    #
    # def get_region_ids(self):
    #     return self.get_json("get_universe_regions")
    #
    # def get_regions(self):
    #     list = []
    #     ids = self.get_region_ids()
    #     for id in ids:
    #         data = self.get_json(
    #             "get_universe_regions_region_id", region_id=id, language="en-us"
    #         )
    #         list.append(data)
    #     return list

    def get_universe_system_kills(self):
        systems = self.universe_api.get_universe_systems()

        empty_kills = []
        for system in systems:
            empty = {"npc_kills": 0, "pod_kills": 0, "ship_kills": 0}
            empty["system_id"] = system
            empty_kills.append(empty)

        system_kills = self.universe_api.get_universe_system_kills()
        for system_kill in system_kills:
            for empty_kill in empty_kills:
                if empty_kill["system_id"] == system_kill["system_id"]:
                    empty_kill["npc_kills"] = system_kill["npc_kills"]
                    empty_kill["pod_kills"] = system_kill["pod_kills"]
                    empty_kill["ship_kills"] = system_kill["ship_kills"]

        return empty_kills

    # def get_types(self):
    #     ids = self.get_json_paged("get_universe_types")
    #     list = []
    #     for id in ids:
    #         data = self.get_json(
    #             "get_universe_types_type_id",
    #             type_id=id,
    #             language="en-us",
    #             expire_timedelta=timedelta(days=30),
    #         )
    #         list.append(data)
    #     return list
    #
    # def get_types_dict(self):
    #     types = self.get_types()
    #     dict = {}
    #     for type in types:
    #         dict[type["type_id"]] = type
    #     return dict
    #
    # def get_json_paged(self, operation_id, **parameters):
    #     max_page = self.get_max_page(operation_id, **parameters)
    #     list = []
    #     for page in range(1, max_page + 1):
    #         data = self.get_json(
    #             operation_id,
    #             page=page,
    #             **parameters,
    #         )
    #         list.extend(data)
    #     return list
    #
    # def get_json(self, operation_id, **parameters):
    #     return self.api.get_response_from(operation_id, **parameters).json
    #
    # def get_max_page(self, operation_id, **parameters):
    #     response = self.api.get_response_from(operation_id, page=1, **parameters)
    #     return response.header["x-pages"][0]
