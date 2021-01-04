"""
    poetry-template.py
    ------------------

    Runs the project.

    :copyrgiht: 2019 MislavJaksic
    :license: MIT License
"""
import sys

from eve_tools.eve_datastore import EveDatastore
from eve_tools.eve_calculator import EveCalculator
from eve_tools.helper.data_frame import DataFrame


def main(args):
    """main() will be run if you run this script directly"""
    with EveCalculator() as calc:
        with EveDatastore() as datastore:
            derelik_contracts = datastore.get_region_contracts(
                calc.region_name_to_id("Derelik")
            )

    dataframe = DataFrame("json", derelik_contracts)
    dataframe.to_csv("derelik_contracts.csv")

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
