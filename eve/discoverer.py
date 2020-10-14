from functools import lru_cache
from getter import Getter

corp_store_error_value = {
    "error": "No loyalty point store found for the provided corporation"
}


class Discoverer(object):
    def __init__(self):
        self.getter = Getter()

    def corp_id_to_corp_name(self, corp_id):
        return self.getter.get_corp_info(corp_id)["name"]

    @lru_cache(maxsize=1)
    def get_all_corp_store_offers(self):
        corp_ids = self.getter.get_corp_npccorps_ids()
        corp_stores = []
        for id in corp_ids:
            corp_store = self.getter.get_corp_store_offers(id)
            if corp_store != corp_store_error_value:
                for dict in corp_store:
                    dict["corporation_id"] = id
                corp_stores.extend(corp_store)

        return corp_stores

    @lru_cache(maxsize=1000)
    def item_id_top_sell_value(self, item_id):
        if self.type_id_to_market_group_id(item_id):
            orders = self.get_all_market_region_item_order_type(
                self.region_name_to_id("The Forge"), item_id, "sell"
            )
            top_sell = orders[0]["price"]
            for order in orders:
                if order["price"] < top_sell:
                    top_sell = order["price"]

            return top_sell
        return -1

    def get_all_market_region_item_order_type(self, region_id, item_id, order_type):
        orders = []
        order_page = True
        page = 1
        while order_page:
            order_page = self.getter.get_market_region_item_order_type_page(
                region_id, item_id, order_type, page
            )
            orders.extend(order_page)
            page += 1

        return orders

    def region_name_to_id(self, region_name):
        return self.get_region_name_to_id_dict()[region_name]

    def get_region_name_to_id_dict(self):
        dict = {}
        region_ids = self.getter.get_universe_region_ids()
        for id in region_ids:
            region_info = self.getter.get_universe_region_info(id)
            dict[region_info["name"]] = region_info["region_id"]

        return dict

    def type_id_to_market_group_id(self, type_id):
        for type_info in self.get_all_type_infos():
            if type_id == type_info["type_id"]:
                return type_info.get_uri_to_file_if_stale("market_group_id")

    def type_name_to_type_id(self, type_name):
        for type_info in self.get_all_type_infos():
            if type_name == type_info["name"]:
                return type_info["type_id"]

    def type_id_to_type_name(self, type_id):
        for type_info in self.get_all_type_infos():
            if type_id == type_info["type_id"]:
                return type_info["name"]

    @lru_cache(maxsize=1)
    def get_all_type_infos(self):
        type_infos = []
        for type_id in self.get_all_types():
            type_info_page = self.getter.get_universe_type_info(type_id)
            type_infos.append(type_info_page)

        return type_infos

    @lru_cache(maxsize=1)
    def get_all_types(self):
        types = []
        for page in range(1, 40):
            type_page = self.getter.get_universe_type_page(page)
            types.extend(type_page)

        return types
