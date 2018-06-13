class Character:

    def __init__(self, name="undefined"):
        # Stats
        self.max_hp = 100
        self.hp = 100
        self.phys_attack = 2
        self.mag_attack = 10
        self.phys_def = 0
        self.mag_def = 0

        # Equipment
        from src.items.items import Weapon
        from src.items.items import Armor
        self.weapon = Weapon()
        self.armor = Armor()

        # Name
        self.name = name

    def equip_item(self, item):
            if isinstance(item, Weapon):
                self.weapon = item
            else:
                self.armor = item

'''Players'''
class Player(Character):

    def __init__(self, name="undefined"):
        super().__init__(name)
        self.specialization = ""
        self.location = []
        self.flee = False

    def attempt_flee(self, enemy, d):
        if d.roll(1, 20) > enemy.phys_attack:
            print("Successfully fled!")
            self.flee = True
        else:
            print("The monster grabbed you before you could get away.")

    def just_fled(self):
        self.flee = False


'''Monsters'''
class Monster(Character):

    def __init__(self, name="undefined", strength=1):
        super().__init__(name)
        self.strength = strength
        self.flee = False

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
                   self.phys_attack, self.mag_attack))