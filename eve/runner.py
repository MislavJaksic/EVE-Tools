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

from package_one import module_one

error_value = {"error": "No loyalty point store found for the provided corporation"}


def main(args):
    """main() will be run if you run this script directly
    """
    corporation_ids = get_corporation_ids()

    for id in corporation_ids:
        corporation_infos = get_corporation_info(id)

    corporation_stores = get_corporation_store(corporation_ids[0])
    for dict in corporation_stores:
        dict["corporation_id"] = corporation_ids[0]
    for id in corporation_ids[1:]:
        corporation_store = get_corporation_store(id)
        if corporation_store != error_value:
            for dict in corporation_store:
                dict["corporation_id"] = id
            corporation_stores.extend(corporation_store)

    # print(corporation_stores)
    dic_flattened = (flatten_json(d) for d in corporation_stores)
    dataframe = pandas.json_normalize(dic_flattened)
    print(dataframe)
    dataframe = dataframe.drop_duplicates()
    dataframe = dataframe.fillna(-1)
    print(dataframe)
    dataframe.to_csv("all-stores.csv")


def get_corporation_ids():
    filename = "corporation_ids.json"
    if not is_file_exists(filename):
        json = requests.get(
            "https://esi.evetech.net/latest/corporations/npccorps/?datasource=tranquility"
        ).json()
        save_json_to_file(json, filename)

    corporation_ids = load_json_from_file(filename)

    return corporation_ids


def get_corporation_info(id):
    filename = "corporation_info_" + str(id) + ".json"
    if not is_file_exists(filename):
        json = requests.get(
            "https://esi.evetech.net/latest/corporations/"
            + str(id)
            + "/?datasource=tranquility"
        ).json()
        save_json_to_file(json, filename)

    corporation_info = load_json_from_file(filename)

    return corporation_info


def get_corporation_store(id):
    filename = "corporation_store_" + str(id) + ".json"
    if not is_file_exists(filename):
        json = requests.get(
            "https://esi.evetech.net/latest/loyalty/stores/"
            + str(id)
            + "/offers/?datasource=tranquility"
        ).json()
        save_json_to_file(json, filename)

    corporation_store = load_json_from_file(filename)

    return corporation_store


def flatten_json(y):
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


def normalize_data_to_json(raw_data: [list, dict, tuple], parent=""):
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
        result[parent] = float(raw_data) if isinstance(raw_data, Decimal) else raw_data

    # normalise datetime object
    elif isinstance(raw_data, datetime):
        result[parent] = raw_data.strftime("%Y-%m-%d %H:%M:%S")

    # normalise dict and all nested dicts.
    # all nests are joined with double underscore to identify parent key name with it's children
    elif isinstance(raw_data, dict):
        for k, v in raw_data.items():
            k = f"{parent}__{k}" if parent else k
            result.update(normalize_data_to_json(v, parent=k))

    # normalise list and tuple
    elif type(raw_data) in [list, tuple]:
        for i, sub_item in enumerate(raw_data, start=1):
            result.update(normalize_data_to_json(sub_item, f"{parent}__{i}"))

    # any data which did not matched above data types, normalise them using it's __str__
    else:
        result[parent] = str(raw_data)

    return result


def is_file_exists(filename):
    path = pathlib.Path("data/" + filename)
    if path.is_file():
        return True
    else:
        return False


def save_json_to_file(json_data, filename):
    with open("data/" + filename, "w") as file:
        file.write(json.dumps(json_data))


def load_json_from_file(filename):
    json_data = ""
    with open("data/" + filename, "r") as file:
        json_data = json.loads(file.read())

    return json_data


def run():
    """Entry point for the runnable script.
    """
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    """main calls run().
    """
    run()
