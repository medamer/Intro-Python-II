# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item, Weapon

class Room(Item):
    def __init__(self, name, description, item_name=None, item_info=None):
        super().__init__(item_name, item_info)
        self.name = name
        self.description = description
    def get_directions(self):
        print(self.direction)
    def get_item_name(self):
        # if hasattr(self.item_name, "has_a"):
        #     self.item_name = getattr(self.item_name, "has_a")
        # else :
        #     print("This room has no items")
        print(self.item.item_name)
    def get_item_type(slef):
        print(self.item.type)
    def __str__(self):
        print(f"Current Room is {self.name} : \n{self.description} \nThis room contains :{self.item_name}")