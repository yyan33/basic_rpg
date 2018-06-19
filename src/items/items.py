import os.path
import sqlite3


class Item:

    def __init__(self, name):
        self.name = name
        self.display = "undefined"

    @staticmethod
    def load_stats(self, name="undefined", slot="weapon"):
        """Load stats from database with given name"""

        db_name = {'weapon': 'weapons.db', 'armor': 'armors.db'}
        table_name = {'weapon': 'Weapons', 'armor': 'Armors'}

        # Connect to database
        abs_file_path = os.path.join(os.path.dirname(__file__), db_name[slot])
        con = sqlite3.connect(abs_file_path)
        c = con.cursor()

        # Find entry in db
        c.execute("SELECT * FROM {} WHERE name IS '{}'".format(table_name[slot], name))
        data = c.fetchone()

        # Close connection and return data
        c.close()
        return data

    def wants_to_equip(self):
        player_choice = input("Would you like to equip it?")
        if player_choice.upper() == 'Y':
            return True
        elif player_choice.upper() == 'N':
            return False
        else:
            print("Invalid input!")
            return self.ask_if_equip()


class Weapon(Item):

    def __init__(self, name="w_undefined"):
        super().__init__(name)
        self.max = 1
        self.min = 1
        self.num_of_atks = 1

        stats = self.load_stats(self, name=name, slot='weapon')
        self.set_stats(stats=stats)

    def set_stats(self, stats):
        self.display = stats[2]
        self.min = stats[3]
        self.max = stats[4]
        self.num_of_atks = stats[5]


class Armor(Item):

    def __init__(self, name="a_undefined"):
        super().__init__(name)
        self.phys_def = 0
        self.mag_def = 0

        stats = self.load_stats(self, name=name, slot='armor')
        self.set_stats(stats=stats)

    def set_stats(self, stats):
        self.display = stats[2]
        self.phys_def = stats[3]
        self.mag_def = stats[4]

