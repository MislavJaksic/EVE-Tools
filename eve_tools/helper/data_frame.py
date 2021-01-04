import pandas
from flatten_json import flatten


class DataFrame:
    def __init__(self, type, data):
        if type == "json":
            self.df = self.from_json(data)
        else:
            raise Exception("{} is not a supported data type.".format(type))

    def from_json(self, jsons):
        list_of_flat_dicts = list((flatten(d) for d in jsons))
        df = pandas.json_normalize(list_of_flat_dicts)
        return df

    def print_all(self):
        print(self.df.to_string())

    def to_csv(self, file_path):
        self.df.to_csv(file_path)
