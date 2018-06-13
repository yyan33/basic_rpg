from src.actors.classes import *
from src.items.items import *
from src.battle_flow.battle import *


'''============================
MAIN
==============================='''
if __name__ == "__main__":
    x = Player(name="Mike")
    y = Monster(name="Azmodeus",strength=4)
    y.phys_def = 10
    y.mag_def = 10
    y.phys_attack = 10

    die = Dice()
    wpn = Weapon()

    battle(x, y, die)
