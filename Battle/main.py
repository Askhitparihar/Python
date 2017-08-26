from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

# Create Black Magic
fire = Spell("Fire", 8, 80, "Black")
thunder = Spell("Thunder", 8, 160, "Black")
blizzard = Spell("Blizzard", 8, 60, "Black")
meteor = Spell("Meteor", 20, 200, "Black")
quake = Spell("Quake", 14, 140, "Black")

# Create White Magic
cure = Spell("Cure", 12, 120, "White")
cura = Spell("Cura", 18, 200, "White")
curaga = Spell("Curaga", 50, 6000, "White")

playerMagic = [fire, thunder, blizzard, meteor, cure, cura]
enemyMagic = [fire, meteor, curaga]

# Create Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hiPotion = Item("High Potion", "potion", "Heals 100 HP", 100)
superPotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixir = Item("Elixir", "elixer", "Fully restores HP/MP of one party member", 9999)
hiElixer = Item("Mega Elixer", "elixer", "Fully restores HP/MP of all party members", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

playerItems = [{"item": potion, "quantity": 15},
               {"item": hiPotion, "quantity": 5},
               {"item": superPotion, "quantity": 5},
               {"item": elixir, "quantity": 5},
               {"item": hiElixer, "quantity": 2},
               {"item": grenade, "quantity": 5}]

# Instantiate Players
player1 = Person("Valos      :", 1860, 47, 460, 34, playerMagic, playerItems)
player2 = Person("Grahnon    :", 2480, 15, 660, 34, playerMagic, playerItems)
player3 = Person("Meira      :", 1280, 99, 160, 34, playerMagic, playerItems)
enemy1 = Person("DemoGorgon :", 11200, 65, 875, 325, enemyMagic, [])
enemy2 = Person("Malcanthet :", 8500, 130, 560, 325, enemyMagic, [])
enemy3 = Person("Arendagrost:", 6750, 65, 475, 325, enemyMagic, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True

print(bcolors.FAIL + bcolors.BOLD + "!AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    i = 0
    print("==================")

    print("NAME     HP            MP          ")

    for player in players:
        player.getPlayerStats()

    print("\n")
    for enemy in enemies:
        enemy.getEnemyStats()

    for player in players:
        player.chooseAction()
        choice = input("Choose action:")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generateDmg()
            enemy = player.chooseTarget(enemies)
            enemies[enemy].takeDmg(dmg)
            print(bcolors.OKBLUE + "Attacked for " + str(dmg) + " points of damage to " + str(enemies[enemy].name.replace(" ", "")) + "." + bcolors.ENDC)
            if enemies[enemy].getHp() == 0:
                print(str(enemies[enemy].name.replace(" ", "")) + " has been defeated.")
                del enemies[enemy]
        elif index == 1:
            player.chooseMagic()
            magicChoice = int(input("choose magic: ")) - 1
            if itemChoice == -1:
                continue

            spell = player.magic[magicChoice]
            magicDmg = spell.generateDmg()
            currentMp = player.getMp()

            if spell.cost > currentMp:
                print(bcolors.FAIL + "\n Not enough MP." + bcolors.ENDC)
                continue

            player.reduceMp(spell.cost)

            if spell.type == "White":
                player.heal(magicDmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for " + str(magicDmg) + " HP." + bcolors.ENDC)
            elif spell.type == "Black":
                enemy = player.chooseTarget(enemies)
                enemies[enemy].takeDmg(dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals " + str(magicDmg) + " points of damage to " + str(enemies[enemy].name.replace(" ", "")) + "." + bcolors.ENDC)
                if enemies[enemy].getHp() == 0:
                    print(str(enemies[enemy].name.replace(" ", "")) + " has been defeated.")
                    del enemies[enemy]
        elif index == 2:
            player.chooseItem()
            itemChoice = int(input("Choose item: ")) - 1

            if itemChoice == -1:
                continue

            item = player.items[itemChoice]["item"]
            if player.items[itemChoice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
                continue

            player.items[itemChoice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for " + str(item.prop) + " HP." + bcolors.ENDC)
            elif item.type == "elixir":
                player.hp = player.maxHp
                player.mp = player.maxMp
                print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP." + bcolors.ENDC)
            elif item.type == "attack":
                enemy = player.chooseTarget(enemies)
                enemies[enemy].takeDmg(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals " + item.prop + " points of damage to " + str(enemies[enemy].name.replace(" ", "")) + "." + bcolors.ENDC)
                if enemies[enemy].getHp() == 0:
                    print(str(enemies[enemy].name.replace(" ", "")) + " has been defeated.")
                    del enemies[enemy]

    # Check if battle is over #
    defeatedEnemies = 0
    defeatedPlayers = 0

    for enemy in enemies:
        if enemy.getHp() == 0:
            defeatedEnemies += 1

    for player in players:
        if player.getHp() == 0:
            defeatedPlayers += 1

    # Check if Plater won
    if defeatedEnemies == 2:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    # Check if Enemy won
    elif defeatedPlayers == 2:
        print(bcolors.FAIL + "Your enemies have defeated you!" + bcolors.ENDC)
        running = False

    print("\n")
    # Enemy attack phase
    for enemy in enemies:
        enemyChoice = random.randrange(0, 2)

        if enemyChoice == 0:
            # Choose attack
            target = random.randrange(0, 2)
            enemyDmg = enemy.generateDmg()

            players[target].takeDmg(enemyDmg)
            print(enemy.name.replace(" ", "") + " attacks " + players[target].name.replace(" ", "") + " for " + str(enemyDmg) + ".")

        elif enemyChoice == 1:
            spell, magicDmg = enemy.chooseEnemySpell()
            enemy.reduceMp(spell.cost)

            if spell.type == "White":
                enemy.heal(magicDmg)
                print(bcolors.OKBLUE + spell.name + " heals " + enemy.name.replace(" ", "") + " for " + str(magicDmg) + " HP." + bcolors.ENDC)

            elif spell.type == "Black":
                target = random.randrange(0, 3)
                players[target].takeDmg(magicDmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals " + str(magicDmg) + " points of damage to " + str(players[target].name.replace(" ", "")) + "." + bcolors.ENDC)
                if players[target].getHp() == 0:
                    print(str(players[target].name.replace(" ", "")) + " has been defeated.")
                    del players[target]
            #print("Enemy chose " + str(spell) + "damage is " + str(magicDmg))



