from eve_tools.eve_datastore import EveDatastore


class EveCalculator:
    def __init__(self):
        self.datastore = EveDatastore()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    # def __getattr__(self, attribute):
    #     if attribute == "swaggerer":
    #         value = Swaggerer(self.swagger_uri)
    #         setattr(self, attribute, value)
    #         return value
    #     else:
    #         raise AttributeError
    def region_name_to_id(self, name):
        regions = self.datastore.get_regions()
        for region in regions:
            if region["name"] == name:
                return region["region_id"]
        raise Exception("{} is not a Region".format(name))

    def close(self):
        self.datastore.close()
