# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item, Weapon

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        #self.direction = {'n','s','e','w'}
    def get_directions(self):
        print(self.direction)
    def get_item_name(self):
        print(self.item.name)
    def get_item_type(slef):
        print(self.item.type)
    def __str__(self):
        print(f"Current Room is {self.name} : \n{self.description}")