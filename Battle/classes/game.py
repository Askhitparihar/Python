import random
from .magic import Spell


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def generateDmg(self):
        return random.randrange(self.atkl, self.atkh)

    def takeDmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxHp:
            self.hp = self.maxHp

    def getHp(self):
        return self.hp

    def getMaxHp(self):
        return self.maxHp

    def getMp(self):
        return self.mp

    def getMaxMp(self):
        return self.maxMp

    def reduceMp(self, cost):
        self.mp -= cost

    def chooseAction(self):
        i = 1
        print("Actions: ")
        for item in self.actions:
            print(str(i) + ":" + str(item))
            i += 1

    def chooseMagic(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "Magic: " + bcolors.ENDC)
        for spell in self.magic:
            print(str(i) + ":" + str(spell.name) + " (cost:" + str(spell.cost) + ")")
            i += 1