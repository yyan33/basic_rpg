from src.actors.actors import *
from src.items.items import *
from src.battle_flow.battle import *




'''============================
MAIN
==============================='''
if __name__ == "__main__":
    d = Dice()
    x = Player(name="Bob", specialization="Ranger")
    y = Monster(name="Abominable Yeti")

    print('''
    {}
    {}
    {}
    -----'''.format(x.phys_def, x.mag_def, x.hp))

    x.equip_item(item=Weapon('Whip'))
    x.equip_item(item=Armor('Dragonscale'))

    print('''
    {}
    {}
    {}
    -----'''.format(x.phys_def, x.mag_def, x.hp))
