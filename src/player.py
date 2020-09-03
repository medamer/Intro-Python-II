# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    def __str__(self):
        return f" Hello {self.name}!, you are in {self.current_room}"
    def move(self, direction):
        if hasattr(self.current_room, direction):
            self.current_room = getattr(self.current_room, direction)
        else :
            print("ERROR! Cannot move in that direction.")
    def get_room(self, current_room):
        return self.current_room