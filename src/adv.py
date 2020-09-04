from room import Room
from player import Player
from item import Item, Weapon

# Declare all the items:
item = {
    'sword' : Weapon("Sword", "A sharp looking sword. Good for fighting goblins!", 5),
    'knife' : Weapon("Knife", "A wicked looking knife, seems sharp!", 3),
    'stick' : Weapon("Stick", "You could probably hit someone with this stick if you needed to", 3)
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", 'sword'),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", 'knife'),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", 'stick'),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", 'sword'),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", None),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']




# Link items to the rooms:

room['outside'].has_a = item['sword']
room['foyer'].has_a = item['knife']
room['overlook'].has_a = item['stick']
room['narrow'].has_a = item['sword']
room['treasure'].has_a = None

# Make a new player object.
player = Player('Mo', [],room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
import sys


while True:
    print("=====================================")
    print(player.current_room.name)
    print(player.current_room.description)
    print(f"This room has {player.current_room.item_name} \n{player.current_room.item_info}")
    cmd = input("Where do you want to go? ")
    print("=====================================")
    if cmd == 'q':
        break
    elif cmd in {'n', 's', 'e', 'w'}:
        player.move(cmd)
    else:
        print('ERROR!! Invalid input')