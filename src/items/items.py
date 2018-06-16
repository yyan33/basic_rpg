import os.path
import sqlite3


class Item:

    def __init__(self):
        pass

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


class Weapon(Item):

    def __init__(self, name="undefined"):
        super().__init__()
        self.max = 0
        self.min = 0
        self.num_of_atks = 0

        stats = self.load_stats(self, name=name, slot='weapon')
        self.set_stats(stats=stats)

    def set_stats(self, stats):
        self.min = stats[2]
        self.max = stats[3]
        self.num_of_atks = stats[4]


class Armor(Item):

    def __init__(self, name="undefined"):
        super().__init__()
        self.phys_def = 0
        self.mag_def = 0

        stats = self.load_stats(self, name=name, slot='armor')
        self.set_stats(stats=stats)

    def set_stats(self, stats):
        self.phys_def = stats[2]
        self.mag_def = stats[3]

