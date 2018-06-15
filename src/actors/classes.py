import sqlite3
import os.path

class Character:

    def __init__(self, name="undefined"):
        # Stats
        self.max_hp = 1
        self.hp = 1
        self.phys_atk = 1
        self.mag_atk = 1
        self.phys_def = 1
        self.mag_def = 1
        self.num_of_atks = 1
        self.min_dmg = 1
        self.max_dmg = 1

        # Name
        self.name = name


'''Players'''
class Player(Character):

    def __init__(self, name="undefined"):
        super().__init__(name)
        self.specialization = ""
        self.location = []
        self.flee = False

        # Equipment
        from src.items.items import Weapon
        from src.items.items import Armor
        self.weapon = Weapon()
        self.armor = Armor()

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
                self.weapon = item
            else:
                self.armor = item


'''Monsters'''
class Monster(Character):

    def __init__(self, name="undefined", strength=1):
        super().__init__(name)
        self.strength = strength
        self.flee = False
        self.fetch_stats(name)

    def show_stats(self):
        print('''{}'s stats:
        Max HP: {}
        Current HP: {}
        Phys Defense: {}
        Mag Defense: {}
        Phys Attack: {}
        Mag Attack: {}
        '''.format(self.name, self.max_hp, self.hp,
                   self.phys_def, self.mag_def,
                   self.phys_atk, self.mag_atk))

    def fetch_stats(self, name="undefined"):
        # Find entry in database
        abs_file_path = os.path.join(os.path.dirname(__file__), "monsters.db")
        con = sqlite3.connect(abs_file_path)
        c = con.cursor()
        c.execute("SELECT * FROM Monsters WHERE name IS '{}'".format(name))
        data = c.fetchone()
        print(data)
        self.set_stats(data[2],data[3], data[4], data[5], data[6], data[7], data[8], data[9])
        c.close()


    def set_stats(self, maxHP=1, phys_atk=1, mag_atk=1, phys_def=1, mag_def=1, num_of_atks=1, min_dmg=1, max_dmg=1):
        self.max_hp = maxHP
        self.hp = maxHP
        self.phys_atk = phys_atk
        self.mag_atk = mag_def
        self.phys_def = phys_def
        self.mag_def = mag_def
        self.num_of_atks = num_of_atks
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg