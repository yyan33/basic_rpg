from src.actors.classes import *
from src.items.items import *
from src.battle_flow.battle import *

import sqlite3
import os




'''============================
MAIN
==============================='''
if __name__ == "__main__":
    x = Player("Bob")
    y = Monster("Abominable Yeti")
    print(vars(y))
