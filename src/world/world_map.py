import csv
import re
from src.world.rooms import *


class World:

    def __init__(self, map_file, rooms_text_file):
        self.map = self.load_map(map_file)
        self.rooms = self.populate_rooms(self.map)
        room_texts = self.load_room_text(rooms_text_file)
        self.set_room_text(room_texts)

    @staticmethod
    def load_map(csv_file):
        map = list(csv.reader(open(csv_file)))
        return map

    @staticmethod
    def populate_rooms(map):
        rooms = []

        # Setup regex expression
        parameters_regex = re.compile(r"'(.*?)'")

        # Read through the map, and create room objects in the
        # appropriate spots with correct intro monster/loot
        for row in map:
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

                # Start Room
                elif col.startswith("Start"):
                    temp_row.append(StartRoom())
                # End Room
                elif col.startswith("End"):
                    temp_row.append(EndRoom())

            rooms.append(temp_row)
        return rooms

    @staticmethod
    def load_room_text(rooms_text_file):
        room_texts = list(csv.reader(open(rooms_text_file)))
        return room_texts

    def set_room_text(self, data):
        for j in range(len(self.map)):
            for i in range(len(self.map)):
                # if the room exists
                if self.rooms[j][i]:
                    self.rooms[j][i].text = data[j][i]

    # For debugging purposes
    def print_map(self, x, y):
        for row in self.rooms:
            print("")
            for col in row:
                if id(col) == id(self.rooms[x][y]):
                    print("C", end="")
                elif isinstance(col, EmptyRoom):
                    print("E", end="")
                elif isinstance(col, MonsterRoom):
                    print("M", end="")
                elif isinstance(col, StartRoom):
                    print("S", end="")
                elif isinstance(col, EndRoom):
                    print("X", end="")
                else:
                    print("*", end="")

