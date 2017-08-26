# coding=utf-8
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
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

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
        print("\n" + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "ACTIONS: " + bcolors.ENDC)
        for item in self.actions:
            print("    " + str(i) + ":" + str(item))
            i += 1

    def chooseMagic(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "MAGIC: " + bcolors.ENDC)
        for spell in self.magic:
            print("    " + str(i) + ":" + str(spell.name) + " (cost:" + str(spell.cost) + ")")
            i += 1

    def chooseItem(self):
        i = 1
        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "ITEMS:" + bcolors.ENDC)
        for item in self.items:
            print("    " + str(i) + ", " + item["item"].name + ": " + item["item"].description,
                  + " (x" + str(item["quantity"]) + ")")
            i += 1

    def chooseTarget(self, targets):
        i = 1
        print("\n" + bcolors.FAIL + bcolors.BOLD + "TARGET: " + bcolors.ENDC)
        for target in targets:
            print(str(i) + "." + target.name)
            i += 1
        choice = int(input("Choose enemy: ")) - 1
        return choice

    def getPlayerStats(self):
        print(bcolors.BOLD + str(self.name) + " " +
              bcolors.OKGREEN + str(self.hp) + "/" + str(self.maxHp) +  bcolors.ENDC + "  |  " + bcolors.BOLD +
              bcolors.OKBLUE + str(self.mp) + "/" + str(self.maxMp) + bcolors.ENDC)

    def getEnemyStats(self):
        print(bcolors.BOLD + str(self.name) + " " +
              bcolors.FAIL + str(self.hp) + "/" + str(self.maxHp) +  bcolors.ENDC + "  |  " + bcolors.BOLD +
              bcolors.OKBLUE + str(self.mp) + "/" + str(self.maxMp) + bcolors.ENDC)

    def chooseEnemySpell(self):
        magicChoice = random.randrange(0, len(self.magic))
        spell = self.magic[magicChoice]
        magicDmg = spell.generateDmg()

        pct = self.hp / self.maxHp * 100

        if self.mp < spell.cost or spell.type == "White" and pct  > 50:
            self.chooseEnemySpell()
        else:
            return spell, magicDmg