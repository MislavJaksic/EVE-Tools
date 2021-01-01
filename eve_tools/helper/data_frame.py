import pandas


class DataFrame:
    def __init__(self, type, data):
        if type == "json":
            self.df = self.from_json(data)
        else:
            raise Exception("{} is not a supported data type.".format(type))

    def from_json(self, jsons):
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

    def to_csv(self, file_path):
        self.df.to_csv(file_path)
