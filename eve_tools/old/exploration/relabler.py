start_id = 1


class DataBlock(object):
    def __init__(self, id, security, type, faction, level):
        self.id = id
        self.security = security
        self.type = type
        self.faction = faction
        self.level = level
        self.item_quantity = {}

    def set_item_quantity(self, item_quantity):
        self.item_quantity = item_quantity
        self.item_quantity = dict(
            sorted(self.item_quantity.items(), key=lambda item: item[0])
        )

    def __str__(self):
        output = ""
        for key in self.item_quantity.keys():
            output = output + str(self.id) + "$"
            output = output + self.security + "$"
            output = output + self.type + "$"
            output = output + self.faction + "$"
            output = output + self.level + "$"
            output = output + key + "$"
            output = output + str(self.item_quantity[key]) + "\n"

        output = output[:-1]
        return output


with open("data.txt", "r") as file:
    summer = {}
    new_id = start_id
    previous_id = -1
    for line in file:
        words = line.split("\t")
        current_id, security, type, faction, level, item, quantity = words
        if previous_id != current_id:
            if summer:
                block.set_item_quantity(summer)
                print(block)
                summer = {}
            block = DataBlock(new_id, security, type, faction, level)
            new_id += 1
        previous_id = current_id
        if summer.get(item):
            summer[item] += int(quantity)
        else:
            summer[item] = int(quantity)

    if summer:
        block.set_item_quantity(summer)
        print(block)
