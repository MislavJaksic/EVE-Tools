"""
    poetry-template.py
    ------------------

    Runs the project.

    :copyrgiht: 2019 MislavJaksic
    :license: MIT License
"""
import sys
import json

from eve_tools.eve_datastore import EveDatastore
from eve_tools.eve_calculator import EveCalculator
from eve_tools.helper.data_frame import DataFrame
from eve_tools.data_layer.sqlite_connection import SQLiteConnection


def main(args):
    """main() will be run if you run this script directly"""

    with EveDatastore() as datastore:
        kills = datastore.get_kills()

    dataframe = DataFrame("json", kills)
    dataframe.to_csv("kills.csv")

    # with SQLiteConnection("./sde/sqlite-20210127.db") as db:
    #     pass

    # with EveCalculator() as calc:
    #     with EveDatastore() as datastore:
    #         derelik_blueprints = datastore.get_region_item_exchange_blueprints(
    #             calc.region_name_to_id("Derelik")
    #         )
    # for contract_blueprint in derelik_blueprints:
    #     print(contract_blueprint)

    # dataframe = DataFrame("json", derelik_blueprints)
    # dataframe.to_csv("derelik_blueprints.csv")

    # lp_db_gen = LPDBGenerator()
    # # lp_db_gen.to_csv("all-stores.csv")
    # # save_unique_ids(lp_db_gen)
    #
    # ids = [int(x) for x in get_unique_ids(lp_db_gen)[0].tolist()]
    # ids.sort()
    # print(ids)
    # getter = APIGetter()
    # for id in ids:
    #     print(getter.get_market_region_item_history(10000002, id))


def run():
    """Entry point for the runnable script."""
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    """main calls run()."""
    run()
