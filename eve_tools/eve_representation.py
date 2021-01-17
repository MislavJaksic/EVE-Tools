class EveContract:
    def __init__(self, metadata):
        self.metadata = metadata


class EveItemExchange(EveContract):
    def __init__(self, metadata, items):
        super(EveItemExchange, self).__init__(metadata)
        self.items = items

    def __repr___(self):
        return self.__str__()

    def __str__(self):
        display_metadata = {
            k: self.metadata[k] for k in self.metadata.keys() & {"contract_id", "price"}
        }
        display_items = []
        for item in self.items:
            bigger = {
                k: item[k]
                for k in item.keys()
                & {
                    "is_blueprint_copy",
                    "material_efficiency",
                    "runs",
                    "time_efficiency",
                    "type",
                }
            }

            bigger["type"] = {
                k: bigger["type"][k] for k in bigger["type"].keys() & {"name"}
            }

            display_items.append(bigger)
        return str({"metadata": display_metadata, "items": display_items})
