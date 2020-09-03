

class Item:
    def __init__(self, name, info):
        self.name = name
        self.info = info

class Weapon(Item):
    def __init__(self, name, info, weight):
        super().__init__(name, info)
        self.weight = weight