from src.actors.actors import Monster
from src.items.items import *


class Room:

    def __init__(self, loot_name=None, text=""):
        if loot_name:
            print(loot_name)
            self.loot = self.load_loot(loot_name)
        else:
            self.loot = None
        self.text = text
        self.visited = False

    def show_intro(self):
        print(self.text)

    @staticmethod
    def load_loot(loot):
        if loot.startswith("w_"):
            return Weapon(loot)
        elif loot.startswith("a_"):
            return Armor(loot)

    def loot_sequence(self):
        self.loot_text(self.loot)
        return self.loot

    @staticmethod
    def loot_text(loot):
        print("You found a {} in the room. Its stats are ".format(loot.display), end="")
        if isinstance(loot, Weapon):
            print("{}-{} DMG, {} attacks per round.".format(loot.min, loot.max, loot.num_of_atks))
        elif isinstance(loot, Armor):
            print("Physical Defense: {}\nMagical Defense: {}".format(loot.phys_def, loot.mag_def))


class MonsterRoom(Room):
    def __init__(self, loot=None, name='undefined', strength='1'):
        super().__init__(loot)
        self.monster = Monster(strength='{}'.format(strength))


class EmptyRoom(Room):
    def __init__(self, loot=None):
        super().__init__(loot)


class StartRoom(Room):
    def __init__(self):
        super().__init__()
        self.text = ''' You wake up in a dark room. You find yourself with a simple, worn sword. The only way out is forward.
                    '''
        self.show_intro()

class EndRoom(Room):
    def __init__(self):
        super().__init__()
        self.text = '''
                        Finally. You can feel a light breeze coming from the other side of
                        the room. It looks like you live to fight another day.
                    '''

    @staticmethod
    def end_game():
        quit()