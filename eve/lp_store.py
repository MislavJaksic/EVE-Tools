from functools import lru_cache
from discoverer import Discoverer
from getter import Getter

corp_store_error_value = {
    "error": "No loyalty point store found for the provided corporation"
}


class LPStore(object):
    def __init__(self):
        self.getter = Getter()
        self.disco = Discoverer()

    def get_offer_isk_per_lp_sell_sell_profit(self, offer):
        return self.get_offer_sell_sell_profit(offer) / offer["lp_cost"]

    def get_offer_sell_sell_profit(self, offer):
        return (
            self.get_offer_sell_value(offer)
            - self.get_required_items_sell_value(offer)
            - offer["isk_cost"]
        )

    def get_offer_sell_value(self, offer):
        return self.disco.item_id_top_sell_value(offer["type_id"]) * offer["quantity"]

    def get_required_items_sell_value(self, offer):
        sell_value = 0
        for required_item in offer["required_items"]:
            sell_value += (
                self.disco.item_id_top_sell_value(required_item["type_id"])
                * required_item["quantity"]
            )
        return sell_value

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

    @lru_cache(maxsize=1)
    def get_all_corp_infos(self):
        corp_ids = self.getter.get_corp_npccorps_ids()
        corp_infos = []
        for id in corp_ids:
            corp_info = self.getter.get_corp_info(id)
            corp_infos.extend(corp_info)

        return corp_infos
