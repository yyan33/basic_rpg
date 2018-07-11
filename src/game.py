from src.actors.actors import *
from src.items.items import *
from src.battle_flow.battle import *
from src.world.world_map import *
from src.world.navigation import *
from src.world.rooms import *

from random import choice

'''============================
MAIN - Hello World
==============================='''
if __name__ == "__main__":
    d = Dice()
    x = Player(name="Bob", specialization="badass")
    y = Monster(strength="2")

    # world = World(map_file='world/map.csv', rooms_text_file='world/room_text.csv')
    world = World(num_of_col=6, num_of_row=7, min_num_of_rooms=20)
    nav = Navigator(world)

    while True:
        nav.change_rooms()
        interact_with_room(nav.current_room, x)


