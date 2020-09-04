

class Item:
    def __init__(self, item_name, item_info):
        self.item_name = item_name
        self.item_info = item_info

class Weapon(Item):
    def __init__(self, item_name, item_info, weight):
        super().__init__(item_name, item_info)
        self.weight = weight