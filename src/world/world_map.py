from src.actors.actors import *
import csv
import re


class Room:

    def __init__(self, loot=None, text=""):
        if loot == '':
            self.loot = None
        else:
            self.loot = loot
        self.text = text

    def show_text(self):
        print(self.text)


class MonsterRoom(Room):
    def __init__(self, loot=None, name=Monster()):
        super().__init__(loot)
        self.monster = Monster(name='{}'.format(name))


class EmptyRoom(Room):
    def __init__(self, loot=None):
        super().__init__(loot)


def load_tiles(csv_file):
    world = list(csv.reader(open(csv_file)))
    return world


def populate_rooms(tiles):
    result = []

    # Setup regex expressions
    parameters_regex = re.compile(r"'(.*?)'")

    # Read through the map, and create room objects in the
    # appropriate spots with correct monster/loot
    for row in tiles:
        temp_row = []
        for col in row:
            # Fetch parameters
            parameters = parameters_regex.findall(col)

            # Blank Tiles
            if col == '':
                temp_row.append(None)

            #     Monster Rooms
            elif col.startswith("Mon"):
                if len(parameters) > 1:
                    temp_row.append(MonsterRoom(name=parameters[0], loot=parameters[1]))
                else:
                    temp_row.append(MonsterRoom(name=parameters[0]))

            # Empty Rooms
            elif col.startswith("Emp"):
                if len(parameters) > 0:
                    temp_row.append(EmptyRoom(loot=parameters[0]))
                else:
                    temp_row.append(EmptyRoom())

        result.append(temp_row)
    return result
