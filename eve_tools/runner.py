"""
    poetry-template.py
    ------------------

    Runs the project.

    :copyrgiht: 2019 MislavJaksic
    :license: MIT License
"""
import sys
from datetime import datetime

# from eve_tools.eve_calculator import EveCalculator

# from eve_tools.data_layer.sqlite_connection import SQLiteConnection
from eve_tools.helper.eve_datastore import EveDatastore
from eve_tools.helper.data_frame import DataFrame

log_message = "update?={update}"


def main(args):
    """main() will be run if you run this script directly"""
    datastore = EveDatastore()
    kills = datastore.get_universe_system_kills()

    dataframe = DataFrame("json", kills)
    dataframe.to_csv("kills" + str(datetime.now().hour) + str(datetime.now().minute) + ".csv")

    # from __future__ import print_function
    # import time
    # from eve_tools import swagger_client
    # from eve_tools.swagger_client.rest import ApiException
    # from pprint import pprint
    #
    # # create an instance of the API class
    # api_instance = swagger_client.UniverseApi()
    # datasource = 'tranquility'  # str | The server name you would like data from (optional) (default to tranquility)
    # if_none_match = 'if_none_match_example'  # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    #
    # try:
    #     # Get system kills
    #     api_response = api_instance.get_universe_system_kills(datasource=datasource, if_none_match=if_none_match)
    #     pprint(api_response)
    # except ApiException as e:
    #     print("Exception when calling UniverseApi->get_universe_system_kills: %s\n" % e)

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
    #
    # dataframe = DataFrame("json", kills)
    # dataframe.to_csv("kills.csv")


def run():
    """Entry point for the runnable script."""
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    """main calls run()."""
    run()
