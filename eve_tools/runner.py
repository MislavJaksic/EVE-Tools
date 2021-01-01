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
import numpy

from api_getter import APIGetter
from eve_tools.discoverer import Discoverer
from eve_tools.lp_store import LPStore
from eve_tools.lp_bd_generator import LPDBGenerator, get_unique_ids, save_unique_ids


def main(args):
    """main() will be run if you run this script directly"""

    lp_db_gen = LPDBGenerator()
    # lp_db_gen.to_csv("all-stores.csv")
    # save_unique_ids(lp_db_gen)

    ids = [int(x) for x in get_unique_ids(lp_db_gen)[0].tolist()]
    ids.sort()
    print(ids)
    getter = APIGetter()
    for id in ids:
        print(getter.get_market_region_item_history(10000002, id))


def run():
    """Entry point for the runnable script."""
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    """main calls run()."""
    run()
