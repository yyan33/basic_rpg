def attack_success(d, offense=1, defense=1):
    """Attempt to land an attack. Offense is attacker's, defense is defender's"""
    atk = d.roll(1, 20) + offense
    if atk > defense:
        print("Attack success!")
        return True
    else:
        print("Attack missed.")
        return False


'''Damage opponent'''
def damage(defender, d, min=1, max=1, num_of_atks=1, mag_atk=0):
    dmg = 0
    # If its a magic attack
    if mag_atk > 0:
        dmg = mag_atk - defender.mag_def
    # Otherwise a physical attack
    else:
        for i in range(num_of_atks):
            dmg += d.roll(min, max)
    defender.hp -= dmg
    if defender.hp < 0:
        print("{} took {} damage. He is dead!".format(defender.name, dmg))
    elif dmg < 0:
        print("{} was resistant to your spell.".format(defender.name))
    else:
        print("{} took {} damage. He has {} hp remaining.".format(defender.name, dmg, defender.hp))