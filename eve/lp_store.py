from discoverer import Discoverer


class LPStore(object):
    def __init__(self):
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
