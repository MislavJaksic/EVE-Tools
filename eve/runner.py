"""
    poetry-template.py
    ------------------

    Runs the project.

    :copyrgiht: 2019 MislavJaksic
    :license: MIT License
"""
import sys
import datetime
import pandas

from getter import Getter
from discoverer import Discoverer
from lp_store import LPStore


class TableMaker(object):
    def flatten_json(self, y):
        out = {}

        def flatten(x, name=""):
            if type(x) is dict:
                for a in x:
                    flatten(x[a], name + a + "_")
            elif type(x) is list:
                i = 0
                for a in x:
                    flatten(a, name + str(i) + "_")
                    i += 1
            else:
                out[name[:-1]] = x

        flatten(y)
        return out

    def normalize_data_to_json(self, raw_data: [list, dict, tuple], parent=""):
        from datetime import datetime
        from decimal import Decimal

        result = {}
        # key name normalise to snake case (single underscore)
        parent = parent.lower().replace(" ", "_") if isinstance(parent, str) else parent
        if isinstance(parent, str) and parent.startswith("__"):
            # if parent has no parent remove double underscore and treat as int if digit else as str
            # treating as int is better if passed data is a list so you output is index based dict
            parent = (
                int(parent.lstrip("_"))
                if parent.lstrip("_").isdigit()
                else parent.lstrip("_")
            )

        # handle str, int, float, and decimal.
        # you can easily add more data types as er your data
        if type(raw_data) in [str, int, float, Decimal]:
            result[parent] = (
                float(raw_data) if isinstance(raw_data, Decimal) else raw_data
            )

        # normalise datetime object
        elif isinstance(raw_data, datetime):
            result[parent] = raw_data.strftime("%Y-%m-%d %H:%M:%S")

        # normalise dict and all nested dicts.
        # all nests are joined with double underscore to identify parent key name with it's children
        elif isinstance(raw_data, dict):
            for k, v in raw_data.items():
                k = f"{parent}__{k}" if parent else k
                result.update(self.normalize_data_to_json(v, parent=k))

        # normalise list and tuple
        elif type(raw_data) in [list, tuple]:
            for i, sub_item in enumerate(raw_data, start=1):
                result.update(self.normalize_data_to_json(sub_item, f"{parent}__{i}"))

        # any data which did not matched above data types, normalise them using it's __str__
        else:
            result[parent] = str(raw_data)

        return result


def main(args):
    """main() will be run if you run this script directly
    """

    getter = Getter()
    disco = Discoverer()
    print(getter.get_corp_npccorps_ids(stale_after=datetime.timedelta(seconds=1)))
    for id in getter.get_corp_npccorps_ids():
        print(str(id) + ":" + disco.corp_id_to_corp_name(id))

    # print(getter.get_universe_type_info(44))

    # # print(disco.type_name_to_type_id("Tritanium"))
    # # print(disco.type_id_to_type_name(34))
    # corp_stores = disco.get_all_corp_store_offers()
    # # print(corp_stores[0])
    # # print(disco.item_id_top_sell_value(23047))
    #
    # lp_store = LPStore()
    # # print(lp_store.get_offer_isk_per_lp_sell_sell_profit(corp_stores[0]))
    # for offer in corp_stores:
    #     print(disco.type_id_to_type_name(offer["type_id"]))
    #     print(disco.type_id_to_market_group_id(offer["type_id"]))
    #     print(lp_store.get_offer_isk_per_lp_sell_sell_profit(offer))

    # corp_stores = disco.get_all_corp_store_offers()
    #
    # table_maker = TableMaker()
    #
    # dic_flattened = (table_maker.flatten_json(d) for d in corp_stores)
    # dataframe = pandas.json_normalize(dic_flattened)
    # print(dataframe)
    # dataframe = dataframe.drop_duplicates()
    # dataframe = dataframe.fillna(-1)
    # print(dataframe)
    # dataframe.to_csv("all-stores.csv")

    # region_ids = getter.get_universe_region_ids()
    # print(region_ids)
    #
    # for id in region_ids:
    #     getter.get_universe_region_info(id)
    #
    # types = getter.get_all_types()
    # print(types)
    # count = 0
    # for type in types:
    #     info = getter.get_universe_type_info(type)
    #     count += 1
    #     if count % 10 == 0:
    #         print(info)

    # disco = Discoverer()
    # corp_stores = disco.get_all_corp_stores()
    # print(corp_stores[0])
    # dict = disco.get_region_name_to_id_dict()
    # forge_id = dict["The Forge"]
    # print(forge_id)
    # disco.item_id_to_top_sell_price(43)
    #
    # types = trans.get_all_types()
    # count = 0
    # for item_id in types:
    #     info = getter.get_market_region_item_history(forge_id, item_id)
    #     count += 1
    #     if count % 10 == 0:
    #         print(info)


def run():
    """Entry point for the runnable script.
    """
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    """main calls run().
    """
    run()
