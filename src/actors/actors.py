import os.path
from src.items.items import *
from random import choice


class Character:

    def __init__(self, name="undefined"):
        # Stats
        self.max_hp = 1
        self.hp = 1
        self.phys_atk = 1
        self.mag_atk = 1
        self.phys_def = 1
        self.mag_def = 1
        self.num_of_atks = 0
        self.min_dmg = 0
        self.max_dmg = 0
        self.flee = False

        # Name
        self.name = name

    def fetch_stats(self, name="undefined", actor="pc", strength="1"):
        """Load stats from database with given name"""

        db_name = {'npc': 'monsters.db', 'pc': 'player_classes.db'}
        table_name = {'npc': 'Monsters', 'pc': 'Classes'}

        # Connect to database
        abs_file_path = os.path.join(os.path.dirname(__file__), db_name[actor])
        con = sqlite3.connect(abs_file_path)
        c = con.cursor()

        # Find entry in db by name
        if actor == 'pc':
            c.execute("SELECT * FROM {} WHERE name IS '{}'".format(table_name[actor], name))
            data = c.fetchone()
        elif actor == 'npc':
            c.execute("SELECT * FROM {} WHERE strength is '{}'".format(table_name[actor], strength))
            data = c.fetchall()
            data = choice(data)


        # Load stats
        if actor == 'pc':
            self.set_stats(max_hp=data[2], phys_atk=data[3], mag_atk=data[4],
                           phys_def=data[5], mag_def=data[6], name=self.name)
        else:
            self.set_stats(max_hp=data[2], phys_atk=data[3], mag_atk=data[4], phys_def=data[5],
                  mag_def=data[6], num_of_atks=data[7], min_dmg=data[8], max_dmg=data[9], name=data[1])

        # Close connection
        c.close()

    def set_stats(self, name="undefined", max_hp=None, phys_atk=None, mag_atk=None, phys_def=None,
                  mag_def=None, num_of_atks=None, min_dmg=None, max_dmg=None):
        self.max_hp = max_hp
        self.hp = max_hp
        self.phys_atk = phys_atk
        self.mag_atk = mag_atk
        self.phys_def = phys_def
        self.mag_def = mag_def
        self.num_of_atks = num_of_atks
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.name = name


class Player(Character):
    """Player Controlled Characters"""
    def __init__(self, name="undefined", specialization="badass"):
        super().__init__(name)
        self.specialization = specialization
        self.flee = False

        # Load class stats
        self.fetch_stats(name=specialization, actor="pc")

        # Equipment
        self.weapon = Weapon()
        self.armor = Armor()
        self.equip_item(Weapon())
        self.equip_item(Armor())

    def attempt_flee(self, enemy, d):
        if d.roll(1, 20) > enemy.phys_atk:
            print("Successfully fled!")
            self.flee = True
        else:
            print("The monster grabbed you before you could get away.")

    def just_fled(self):
        self.flee = False

    def equip_item(self, item):
            if isinstance(item, Weapon):
                self.update_weapon(new_weapon=item)
                self.weapon = item
            else:
                self.update_armor(new_armor=item)
                self.armor = item

    def update_weapon(self, new_weapon):
        self.num_of_atks = new_weapon.num_of_atks
        self.min_dmg = new_weapon.min
        self.max_dmg = new_weapon.max

    def update_armor(self, new_armor):
        self.phys_def = self.phys_def - self.armor.phys_def + new_armor.phys_def
        self.mag_def = self.mag_def - self.armor.mag_def + new_armor.mag_def


class Monster(Character):
    """Non-playable characters"""

    def __init__(self, name="undefined", strength='1'):
        super().__init__(name)
        self.strength = strength

        # Load monster stats
        self.fetch_stats(name=name, actor="npc", strength=strength)

    def show_stats(self):
        """Prints out monster's stats when inspected by player"""
        print("""{}'s stats:
        Max HP: {}
        Current HP: {}
        Phys Defense: {}
        Mag Defense: {}
        Phys Attack: {}
        Mag Attack: {}
        """.format(self.name, self.max_hp, self.hp,
                   self.phys_def, self.mag_def,
                   self.phys_atk, self.mag_atk))
