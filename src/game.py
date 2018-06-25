from src.actors.actors import *
from src.items.items import *
from src.battle_flow.battle import *
from src.world.world_map import *
from src.world.navigation import *
from src.world.rooms import *

from random import choice


'''============================
MAIN
==============================='''
if __name__ == "__main__":
    d = Dice()
    x = Player(name="Bob", specialization="Ranger")
    y = Monster(strength="2")

    world = World(num_of_row=4, num_of_col=8, min_num_of_rooms=20)
    # print_map(world)
    # nav = Navigator(world)
    # while True:
    #     nav.change_rooms()
    #     interact_with_room(nav.current_room, x)


