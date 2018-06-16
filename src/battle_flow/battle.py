from time import sleep
from random import randint

from src.actors.actors import Player
from src.battle_flow.attack_round import *

'''==============================
BATTLE FUNCTIONS
=============================='''
'''Start battle'''
def battle(pc, npc, d):
    # p1 = attacker, p2 = defender
    attacker = pc
    defender = npc

    while attacker.hp > 0:
        if attacker.flee:
            attacker.just_fled()
            break
        else:
            turn(attacker, defender, d)
            # swap whose turn it is
            attacker, defender = defender, attacker
            sleep(1)
            print('''
===============================
        CHANGE TURNS
===============================''')
            sleep(1)
    print("Battle ended!")


'''Turn'''
def turn(attacker, defender, d):
    if isinstance(attacker, Player):
        player_turn(attacker, defender, d)
    else:
        monster_turn(attacker, defender, d)


'''Player actions'''
def player_turn(p, m, d):
    action = input('''
Select your action (1/2/3/4):
1. Physical Attack
2. Magic Attack
3. Inspect Enemy
4. Flee
            ''')

    if action == '1':
        if attack_success(offense=p.phys_atk, defense=m.phys_def, d=d):
            damage(wpn=p.weapon, defender=m, d=d)

    elif action == '2':
        if attack_success(offense=p.mag_atk, defense=m.mag_def, d=d):
            damage(mag_atk=p.mag_atk, defender=m, d=d)

    elif action == '3':
        m.show_stats()

    elif action == '4':
        p.attempt_flee(m, d)

    else:
        print("Invalid input. Try again.")
        player_turn(p, m, d)


'''Monster turn'''
def monster_turn(m, p, d):
    if p.phys_def > p.mag_def:
        if attack_success(offense=m.mag_atk, defense=p.mag_def, d=d):
            damage(mag_atk=m.mag_atk, defender=p, d=d)
    else:
        if attack_success(offense=m.phys_atk, defense=p.phys_def, d=d):
            damage(wpn=m.weapon, defender=p, d=d)


'''==============================
DICE
=============================='''
class Dice:

    def __init__(self):
        pass

    def roll(self, min, max):
        result = randint(min, max)
        print("\nDice roll: {}".format(result))
        sleep(1)
        return result