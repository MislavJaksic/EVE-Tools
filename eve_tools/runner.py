"""
    poetry-template.py
    ------------------

    Runs the project.

    :copyrgiht: 2019 MislavJaksic
    :license: MIT License
"""
import sys
from datetime import datetime

from eve_tools.helper.data_frame import DataFrame
from eve_tools.helper.eve_datastore import EveDatastore

# from eve_tools.eve_calculator import EveCalculator
# from eve_tools.data_layer.sqlite_connection import SQLiteConnection

log_message = "update?={update}"


def main(args):
    """main() will be run if you run this script directly"""
    save_system_kills()


def save_system_kills():
    datastore = EveDatastore()
    kills = datastore.get_universe_system_kills()

    dataframe = DataFrame("json", kills)
    dataframe.to_csv("kills" + str(datetime.now().hour) + str(datetime.now().minute) + ".csv")


def run():
    """Entry point for the runnable script."""
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    """main calls run()."""
    run()
