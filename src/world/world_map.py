import csv
import re
from src.world.rooms import *
from src.world.generate_world import generate_random_map
from itertools import chain


class World:

    def __init__(self, map_file=None, rooms_text_file=None, num_of_row=0, num_of_col=0, min_num_of_rooms=0):
        if map_file:
            self.map = self.load_map(map_file)
            room_texts = self.load_room_text(rooms_text_file)
            self.rooms = self.populate_loaded_rooms(self.map)
            self.set_room_text(room_texts)
        else:
            self.map = generate_random_map(max_row=num_of_row, max_col=num_of_col, min_num_of_rooms=min_num_of_rooms)
            for p in self.map:
                print(p)
            self.rooms = self.create_random_rooms_data(self.map)
            for k in self.map:
                print(k)


    @staticmethod
    def load_map(csv_file):
        map = list(csv.reader(open(csv_file)))
        return map

    @staticmethod
    def populate_loaded_rooms(map):
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

    @staticmethod
    def create_random_rooms_data(map):
        result = []
        # for row
        for i in range(len(map)):
            # for col
            temp_row = []
            for j in range(len(map[i])):
                e = map[i][j]
                if e == 'R':
                    temp_row.append(generate_random_room())
                elif e == '':
                    temp_row.append(None)
                elif e == 'S':
                    temp_row.append(StartRoom())
                elif e == 'E':
                    temp_row.append(EndRoom())
            result.append(temp_row)
        return result

    # For debugging purposes
    def print_map(self, x, y, mode="player"):
        # Print map details
        if mode == "admin":
            for row in self.rooms:
                print("")
                for col in row:
                    # Player current location
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
                        print("■", end="")

        else:
            for row in self.rooms:
                print("")
                for col in row:
                    # Player current location
                    if id(col) == id(self.rooms[x][y]):
                        print("C", end="")
                    # If room exists and visited
                    elif col and col.visited:
                        print("X", end="")
                    else:
                        print("■", end="")



