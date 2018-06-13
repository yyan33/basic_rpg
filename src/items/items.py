'''==============================
WEAPONS
=============================='''
class Weapon:

    def __init__(self, max=100, min=1, num_of_atks=1):
        self.max = max
        self.min = min
        self.num_of_atks = num_of_atks


'''==============================
ARMOR
=============================='''
class Armor:

    def __init__(self, phys_def=1, mag_def=1):
        self.phys_def = phys_def
        self.mag_def = mag_def