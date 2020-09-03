# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, direction):
        self.name = name
        self.description = description
        self.direction = {'n','s','e','w'}
    def get_directions(self):
        print(self.direction)
    def str_directions(self):
        to_str = [str(v) for k, v in self.direction.item()]
        return ' '.join(to_str)
    def __str__(self):
        print(f"Current Room is {self.name} : \n{self.description}")