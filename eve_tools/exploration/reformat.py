import re

start_id = 66


class DataBlock(object):
    def __init__(self, id, security, type, faction, level):
        self.id = id
        self.security = security
        self.type = type
        self.faction = faction
        self.level = level
        self.name_quantity = {}

    def set_name_quantity(self, name_quantity):
        self.name_quantity = name_quantity
        self.name_quantity = dict(
            sorted(self.name_quantity.items(), key=lambda item: item[0])
        )

    def __str__(self):
        output = ""
        for key in self.name_quantity.keys():
            output = output + str(self.id) + "$"
            output = output + self.security + "$"
            output = output + self.type + "$"
            output = output + self.faction + "$"
            output = output + self.level + "$"
            output = output + key + "$"
            output = output + str(self.name_quantity[key]) + "\n"

        output = output[:-1]
        return output


with open("data.txt", "r") as file:
    summer = {}
    id = start_id
    for line in file:
        if line.strip() and line != "EOF\n":
            words = line.split("\t")
            security, type, faction, level, _ = words

            if security:
                block = DataBlock(id, security, type, faction, level)
                id = id + 1
            match = re.search("(^\d+ )(.*)", words[4].strip())

            count = int(match.group(1))
            name = match.group(2)

            if summer.get(name):
                summer[name] = summer[name] + count
            else:
                summer[name] = count
        else:
            block.set_name_quantity(summer)
            print(block)

            summer = {}
