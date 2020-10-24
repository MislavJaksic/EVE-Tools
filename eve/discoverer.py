from functools import lru_cache
from api_getter import APIGetter
import pandas


class Discoverer(object):
    def __init__(self):
        self.getter = APIGetter()

    def corp_id_to_corp_name(self, corp_id):
        return self.getter.get_corp_info(corp_id)["name"]

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

    def market_group_id_to_market_group_name(self, id):
        if not pandas.isna(id):
            return self.get_all_market_group_infos()[id].get("name")
        return None

    def region_name_to_id(self, region_name):
        return self.get_region_name_to_id_dict()[region_name]

    def get_region_name_to_id_dict(self):
        dict = {}
        region_ids = self.getter.get_universe_region_ids()
        for id in region_ids:
            region_info = self.getter.get_universe_region_info(id)
            dict[region_info["name"]] = region_info["region_id"]

        return dict

    def type_id_to_market_group_id(self, id):
        return self.get_all_type_infos()[id].get("market_group_id")

    def type_name_to_type_id(self, type_name):
        for id, info in self.get_all_type_infos():
            if info["name"] == type_name:
                return id

    def type_id_to_type_name(self, id):
        if not pandas.isna(id):
            return self.get_all_type_infos()[id]["name"]
        return None

    @lru_cache(maxsize=1)
    def get_all_market_group_infos(self):
        market_group_infos = {}
        for market_group_id in self.getter.get_market_group_ids():
            market_group_info = self.getter.get_market_group_info(market_group_id)
            market_group_infos[market_group_id] = market_group_info

        return market_group_infos

    @lru_cache(maxsize=1)
    def get_all_type_infos(self):
        type_infos = {}
        for id in self.get_all_type_ids():
            type_info_page = self.getter.get_universe_type_info(id)
            type_infos[id] = type_info_page

        return type_infos

    @lru_cache(maxsize=1)
    def get_all_type_ids(self, stale_after=None):
        types = []
        for page in range(1, 40):
            type_page = self.getter.get_universe_type_page(page, stale_after)
            types.extend(type_page)

        return types
