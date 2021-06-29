import sys

import pandas


# class Dataframe(object):
#     def __init__(self, csv_filename):
#         self.df = pandas.read_csv(csv_filename)
#
#     def drop_columns(self, columns):
#         self.df = self.df.drop(columns, axis=1)
#
#     def drop_duplicates(self):
#         self.df = self.df.drop_duplicates()
#
#     def to_csv(self, csv_filename):
#         self.df.to_csv(csv_filename)

# ["ID", "Security", "Site", "Faction", "Level", "Item", "Quantity"]
def lowsec_count_by_level():
    csv_filename = "lowsec_relic.csv"
    df = pandas.read_csv(csv_filename)
    columns = ["Security", "Site", "Faction", "Item", "Quantity"]
    df = df.drop(columns, axis=1)
    df = df.drop_duplicates()

    df = df.groupby(by=["Level"]).count()

    df.to_csv("lowsec_count_by_level.csv")


def lowsec_relic_by_level_by_item():
    csv_filename = "lowsec_relic.csv"
    df = pandas.read_csv(csv_filename)
    columns = ["ID", "Security", "Site", "Faction"]
    df = df.drop(columns, axis=1)
    df = df.groupby(by=["Level", "Item"]).sum()

    df.to_csv("lowsec_relic_by_level_by_item.csv")


def lowsec_relic_item_quantity():
    csv_filename = "lowsec_relic.csv"
    df = pandas.read_csv(csv_filename)
    columns = ["ID", "Security", "Site", "Faction", "Level"]
    df = df.drop(columns, axis=1)
    df = df.groupby(by=["Item"]).sum()

    df.to_csv("lowsec_relic_item_quantity.csv")


def main(args):
    """main() will be run if you run this script directly"""

    lowsec_count_by_level()
    lowsec_relic_by_level_by_item()
    lowsec_relic_item_quantity()


def run():
    """Entry point for the runnable script."""
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    """main calls run()."""
    run()

    # labels=[
    #     "Security Rating",
    #     "Site Type",
    #     "Pirate Faction",
    #     "Loot Name",
    #     "Quantity",
    # ],
