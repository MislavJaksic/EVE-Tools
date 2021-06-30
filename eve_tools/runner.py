"""
    poetry-template.py
    ------------------

    Runs the project.

    :copyrgiht: 2019 MislavJaksic
    :license: MIT License
"""
import datetime
import sys
from time import sleep

from loguru import logger

from eve_tools.chat.collection import ChatChannelCollection
from eve_tools.chat.parser import ChatChannelParser
from eve_tools.eve_datastore import EveDatastore
# from eve_tools.eve_calculator import EveCalculator
from eve_tools.helper.data_frame import DataFrame

# from eve_tools.data_layer.sqlite_connection import SQLiteConnection

log_message = "update?={update}"


def main(args):
    """main() will be run if you run this script directly"""

    parser = ChatChannelParser()
    collection = ChatChannelCollection(parser, "C:/Users/Korisnik/Documents/EVE/logs/Chatlogs", [])
    collection.filter_by_channel_name("Class")
    for channel in collection.channels:
        print(channel.metadata)
    # datastore = EveDatastore()
    # kills = datastore.get_universe_system_kills()
    #
    # dataframe = DataFrame("json", kills)
    # dataframe.to_csv("kills" + str(datetime.datetime.now().timestamp()) + ".csv")
    #
    # counter = 0
    # while counter < 1000:
    #     counter += 1
    #     sleep(600)
    #     if kills == datastore.get_universe_system_kills():
    #         updated = False
    #     else:
    #         updated = True
    #         dataframe = DataFrame("json", kills)
    #         dataframe.to_csv(
    #             "kills" + str(datetime.datetime.now().timestamp()) + ".csv"
    #         )
    #
    #     logger.info(
    #         log_message,
    #         update=updated,
    #     )
    #
    #     kills = datastore.get_universe_system_kills()

    # dataframe = DataFrame("json", kills)
    # dataframe.to_csv("kills.csv")


def run():
    """Entry point for the runnable script."""
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    """main calls run()."""
    run()
