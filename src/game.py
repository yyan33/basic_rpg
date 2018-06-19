from src.actors.actors import *
from src.items.items import *
from src.battle_flow.battle import *
from src.world.world_map import *
from src.world.navigation import *
from src.world.rooms import *




'''============================
MAIN
==============================='''
if __name__ == "__main__":
    d = Dice()
    x = Player(name="Bob", specialization="Ranger")
    y = Monster(name="Abominable Yeti")

    world = World('world/map.csv', 'world/room_text.csv')
    # print_map(world)

    nav = Navigator(world)
    while True:
        nav.change_rooms()
        interact_with_room(nav.current_room, x)

    pass


