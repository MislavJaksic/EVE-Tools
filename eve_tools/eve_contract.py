class EveContract:
    def __init__(self, metadata):
        self.metadata = metadata


class EveItemExchange(EveContract):
    def __init__(self, metadata, items):
        super(EveItemExchange, self).__init__(metadata)
        self.items = items

    def __str__(self):
        return str({"metadata": self.metadata, "items": self.items})
