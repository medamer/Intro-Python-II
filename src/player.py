# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name, bag,current_room):
        self.name = name
        self.current_room = current_room
        self.bag = []
    def __str__(self):
        return f" Hello {self.name}!, you are in {self.current_room}, bag {self.bag}"
    def move(self, direction):
        if hasattr(self.current_room, f"{direction}_to"):
            self.current_room = getattr(self.current_room, f"{direction}_to")
        else :
            print("ERROR! Cannot move in that direction.")
    def get_room(self, current_room):
        return self.current_room
    def pick_up(self):
        self.inventory.append(self.item_name)
    def get_inventory(self):
        print(self.inventory)