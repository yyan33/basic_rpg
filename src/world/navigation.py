from src.world.world_map import *
from src.battle_flow.battle import *


class Navigator:
    def __init__(self, world):
        self.col_cord = 0
        self.row_cord = 0
        self.world = world
        self.current_room = world.rooms[0][0]
        self.y_max = len(world.map) - 1
        self.x_max = len(world.map) + 1

    def change_rooms(self):
        exit_options = self.check_exits()
        new_room_dir = self.select_room(exit_options)
        self.move_rooms(new_room_dir)

    def check_exits(self):
        exits = []
        # Check if on boundary and if the room exists

        # North
        if self.row_cord - 1 >= 0 and self.world.rooms[(self.row_cord - 1)][self.col_cord]:
                exits.append('N')
        # South
        if self.row_cord + 1 < self.y_max + 1 and self.world.rooms[(self.row_cord + 1)][self.col_cord]:
                exits.append('S')
        # East
        if self.col_cord + 1 < self.x_max:
            if self.world.rooms[self.row_cord][(self.col_cord + 1)]:
                exits.append('E')
        # West
        if self.col_cord - 1 >= 0 and self.world.rooms[self.row_cord][(self.col_cord - 1)]:
                exits.append('W')

        self.world.print_map(self.row_cord, self.col_cord)
        return exits

    def select_room(self, exit_options):
        print("\nAvailable exits: {}".format(','.join(exit_options)))
        direction = input("Enter direction (N/S/E/W): ")
        if direction.upper() not in exit_options:
            self.world.print_map(self.row_cord, self.col_cord)
            print("\nInvalid choice.")
            return self.select_room(exit_options)
        else:
            return direction.upper()

    def move_rooms(self, direction):
        sign = {'N': -1, 'S': 1, 'E': 1, 'W': -1}
        # Update navigator's coordinates
        if direction in ['N', 'S']:
            self.row_cord += sign[direction]
        elif direction in ['E', 'W']:
            self.col_cord += sign[direction]

        # Update current room
        self.current_room = self.world.rooms[self.row_cord][self.col_cord]


def interact_with_room(room, player):
    room.show_intro()
    if room.visited:
        print("You have already been here.")
    else:
        room.visited = True
        if isinstance(room, EndRoom):
            room.end_game()
        elif isinstance(room, MonsterRoom):
            battle(pc=player, npc=room.monster, d=Dice())
        #     If room has loot, display it
        if room.loot:
            loot = room.loot_sequence()
            if loot.wants_to_equip():
                player.equip_item(loot)
                print("Equipped.")
