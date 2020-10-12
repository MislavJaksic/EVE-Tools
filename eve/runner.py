"""
    poetry-template.py
    ------------------

    Runs the project.

    :copyrgiht: 2019 MislavJaksic
    :license: MIT License
"""
import sys
import requests
import pathlib
import pandas
import json
import cachier

relative_cache_path = "data/"

stalness_cutoff = "TODO"

corp_store_error_value = {
    "error": "No loyalty point store found for the provided corporation"
}


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


class EVEGetter(object):
    def __init__(self):
        self.file_cacher = FileCacher()

    def get_corp_npccorps_ids(self):
        filename = "corporation_npccorps_ids.json"
        uri = "https://esi.evetech.net/latest/corporations/npccorps/?datasource=tranquility"

        return self.file_cacher.get(uri, filename)

    def get_corp_info(self, id):
        filename = "corporation_info_{}.json".format(str(id))
        uri = "https://esi.evetech.net/latest/corporations/{}/?datasource=tranquility".format(
            str(id)
        )

        return self.file_cacher.get(uri, filename)

    def get_all_corp_stores(self):
        corp_ids = self.get_corp_npccorps_ids()
        corp_stores = []
        for id in corp_ids:
            corp_store = self.get_corp_store(id)
            if corp_store != corp_store_error_value:
                for dict in corp_store:
                    dict["corporation_id"] = id
                corp_stores.extend(corp_store)

        return corp_stores

    def get_corp_store(self, id):
        filename = "corporation_store_{}.json".format(str(id))
        uri = "https://esi.evetech.net/latest/loyalty/stores/{}/offers/?datasource=tranquility".format(
            str(id)
        )

        return self.file_cacher.get(uri, filename)

    def get_market_region_item_history(self, region_id, item_id):
        filename = "corporation_store_{}.json".format(str(id))
        uri = "https://esi.evetech.net/latest/loyalty/stores/{}/offers/?datasource=tranquility".format(
            str(id)
        )

        return self.file_cacher.get(uri, filename)

    def get_universe_region_ids(self):
        filename = "region_ids.json"
        uri = "https://esi.evetech.net/latest/universe/regions/?datasource=tranquility"

        return self.file_cacher.get(uri, filename)

    def get_region_name_to_id(self):
        dict = {}
        region_ids = self.get_universe_region_ids()
        for id in region_ids:
            region_info = self.get_universe_region_info(id)
            dict[region_info["name"]] = region_info["region_id"]

        return dict

    def get_universe_region_info(self, id):
        filename = "region_info_{}.json".format(str(id))
        uri = "https://esi.evetech.net/latest/universe/regions/{}/?datasource=tranquility".format(
            str(id)
        )

        return self.file_cacher.get(uri, filename)

    def get_all_types(self):
        types = []
        for page in range(1, 40):
            type_page = self.get_universe_type(page)
            types.extend(type_page)

        return types

    def get_universe_type(self, page):
        filename = "type_page_{}.json".format(str(page))
        uri = "https://esi.evetech.net/latest/universe/types/?datasource=tranquility&page={}".format(
            str(page)
        )

        return self.file_cacher.get(uri, filename)

    def get_universe_type_info(self, id):
        filename = "type_info_{}.json".format(str(id))
        uri = "https://esi.evetech.net/latest/universe/types/{}/?datasource=tranquility".format(
            str(id)
        )

        return self.file_cacher.get(uri, filename)


class FileCacher(object):
    def is_file_exists(self, filename):
        path = pathlib.Path(relative_cache_path + filename)
        if path.is_file():
            return True
        else:
            return False

    def get(self, uri, filename):
        if not self.is_file_exists(filename):
            try:
                response = requests.get(uri)
                json = response.json()
                self.save_json_to_file(json, filename)
            except:
                print("Response that caused an error:" + str(response))

        return self.load_json_from_file(filename)

    def is_stale(self, filename, duration):
        pass

    def save_json_to_file(self, json_data, filename):
        with open(relative_cache_path + filename, "w") as file:
            file.write(json.dumps(json_data))

    def load_json_from_file(self, filename):
        json_data = ""
        with open(relative_cache_path + filename, "r") as file:
            json_data = json.loads(file.read())

        return json_data


def main(args):
    """main() will be run if you run this script directly
    """

    getter = EVEGetter()

    # corp_ids = getter.get_corp_npccorps_ids()

    # for id in corp_ids:
    #     corp_infos = getter.get_corp_info(id)

    # corp_stores = getter.get_all_corp_stores()
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

    # dict = getter.get_region_name_to_id()
    # print(dict["The Forge"])
    #
    # types = getter.get_all_types()
    # print(types)
    # count = 0
    # for type in types:
    #     info = getter.get_universe_type_info(type)
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
