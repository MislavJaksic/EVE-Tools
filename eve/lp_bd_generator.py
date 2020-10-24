import pandas
import numpy
from discoverer import Discoverer
from lp_store import LPStore


class LPDBGenerator(object):
    def __init__(self):
        lp_store = LPStore()
        json_offers = lp_store.get_all_corp_store_offers()
        maker = DataframeMaker()
        self.df = maker.json_to_dataframe(json_offers)
        self.disco = Discoverer()
        self.add_all_type_names()
        self.add_corporation_name()
        self.add_market_group_id()
        self.add_market_group_name()
        self.add_empty_columns()
        self.reorder_columns()

    def to_csv(self, filename):
        self.df.to_csv(filename)

    def add_all_type_names(self):
        id_name_column_pairs = [
            ("type_id", "type_name"),
            ("required_items_0_type_id", "required_items_0_item_name"),
            ("required_items_1_type_id", "required_items_1_item_name"),
            ("required_items_2_type_id", "required_items_2_item_name"),
            ("required_items_3_type_id", "required_items_3_item_name"),
            ("required_items_4_type_id", "required_items_4_item_name"),
        ]
        for id_column, name_column in id_name_column_pairs:
            self.add_name_id_column(id_column, name_column)

    def add_name_id_column(self, id_column, name_column):
        type_ids = self.df[id_column].tolist()
        type_names = []
        for id in type_ids:
            type_name = self.disco.type_id_to_type_name(id)
            type_names.append(type_name)

        self.df[name_column] = type_names

    def add_corporation_name(self):
        corporation_ids = self.df["corporation_id"].tolist()
        corporation_names = []
        for id in corporation_ids:
            corporation_name = self.disco.corp_id_to_corp_name(id)
            corporation_names.append(corporation_name)

        self.df["corporation_name"] = corporation_names

    def add_market_group_id(self):
        type_ids = self.df["type_id"].tolist()
        market_group_ids = []
        for id in type_ids:
            market_group_id = self.disco.type_id_to_market_group_id(id)
            market_group_ids.append(market_group_id)

        integer_array = pandas.array(market_group_ids, dtype="Int64")
        self.df["market_group_id"] = integer_array

    def add_market_group_name(self):
        market_group_ids = self.df["market_group_id"].tolist()
        market_group_names = []
        for id in market_group_ids:
            market_group_name = self.disco.market_group_id_to_market_group_name(id)
            market_group_names.append(market_group_name)

        self.df["market_group_name"] = market_group_names

    def add_empty_columns(self):
        empty_columns = [
            "faction_name",
            "buy_value",
            "sell_value",
            "buy_volume",
            "sell_volume",
            "sum_required_items_0_item_buy_value",
            "sum_required_items_0_item_sell_value",
            "sum_required_items_1_item_buy_value",
            "sum_required_items_1_item_sell_value",
            "sum_required_items_2_item_buy_value",
            "sum_required_items_2_item_sell_value",
            "sum_required_items_3_item_buy_value",
            "sum_required_items_3_item_sell_value",
            "sum_required_items_4_item_buy_value",
            "sum_required_items_4_item_sell_value",
            "total_isk_buy_cost",
            "total_isk_sell_cost",
            "profit_sell_to_buy_buy_from_sell",
            "profit_sell_to_sell_buy_from_sell",
            "isk_per_lp_profit_sell_to_buy_buy_from_sell",
            "isk_per_lp_profit_sell_to_sell_buy_from_sell",
        ]
        for col in empty_columns:
            self.df[col] = numpy.nan

    def reorder_columns(self):
        column_order = [
            "offer_id",
            "faction_name",
            "corporation_id",
            "corporation_name",
            "type_id",
            "type_name",
            "market_group_id",
            "market_group_name",
            "quantity",
            "buy_value",
            "sell_value",
            "buy_volume",
            "sell_volume",
            "isk_cost",
            "lp_cost",
            "ak_cost",
            "required_items_0_type_id",
            "required_items_0_item_name",
            "required_items_0_quantity",
            "sum_required_items_0_item_buy_value",
            "sum_required_items_0_item_sell_value",
            "required_items_1_type_id",
            "required_items_1_item_name",
            "required_items_1_quantity",
            "sum_required_items_1_item_buy_value",
            "sum_required_items_1_item_sell_value",
            "required_items_2_type_id",
            "required_items_2_item_name",
            "required_items_2_quantity",
            "sum_required_items_2_item_buy_value",
            "sum_required_items_2_item_sell_value",
            "required_items_3_type_id",
            "required_items_3_item_name",
            "required_items_3_quantity",
            "sum_required_items_3_item_buy_value",
            "sum_required_items_3_item_sell_value",
            "required_items_4_type_id",
            "required_items_4_item_name",
            "required_items_4_quantity",
            "sum_required_items_4_item_buy_value",
            "sum_required_items_4_item_sell_value",
            "total_isk_buy_cost",
            "total_isk_sell_cost",
            "profit_sell_to_buy_buy_from_sell",
            "profit_sell_to_sell_buy_from_sell",
            "isk_per_lp_profit_sell_to_buy_buy_from_sell",
            "isk_per_lp_profit_sell_to_sell_buy_from_sell",
        ]
        self.df = self.df[column_order]

    def fill_na(self):
        self.df = self.df.fillna(-1)

    def __str__(self):
        return str(self.df)


class DataframeMaker(object):
    def json_to_dataframe(self, jsons):
        dic_flattened = (self.flatten_json(d) for d in jsons)
        df = pandas.json_normalize(dic_flattened)
        return df

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


def get_unique_ids(lp_db_gen):
    id_columns = [
        "type_id",
        "required_items_0_type_id",
        "required_items_1_type_id",
        "required_items_2_type_id",
        "required_items_3_type_id",
        "required_items_4_type_id",
    ]

    all_type_ids = []
    for id_column in id_columns:
        type_ids = lp_db_gen.df[id_column].tolist()
        all_type_ids.extend(type_ids)
    unique_ids = pandas.DataFrame(all_type_ids).dropna().drop_duplicates()
    return unique_ids


def save_unique_ids(lp_db_gen):
    get_unique_ids(lp_db_gen).to_csv("unique_ids.csv")
