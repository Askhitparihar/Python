from classes.game import Person, bcolors
from classes.magic import Spell

# Create Black Magic
fire = Spell("Fire", 8, 80, "Black")
thunder = Spell("Thunder", 8, 160, "Black")
blizzard = Spell("Blizzard", 8, 60, "Black")
meteor = Spell("Meteor", 20, 200, "Black")
quake = Spell("Quake", 14, 140, "Black")

# Create White Magic
cure = Spell("Cure", 12, 120, "White")
cura = Spell("Cura", 18, 200, "White")

# Instantiate Players
player = Person(460, 65,60, 34, [fire, thunder, blizzard, meteor, cure, cura])
enemy = Person(1200, 65, 45, 25, [])

running = True

print(bcolors.FAIL + bcolors.BOLD + "!AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("==================")
    player.chooseAction()
    choice = input("Choose action:")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generateDmg()
        enemy.takeDmg(dmg)
        print("Attacked for " + str(dmg) + " points of damage. Enemy HP: " + str(enemy.getHp()))
    elif index == 1:
        player.chooseMagic()
        magicChoice = int(input("choose magic:")) - 1
        spell = player.magic[magicChoice]
        magicDmg = spell.generateDmg()


        currentMp = player.getMp()

        if spell.cost > currentMp:
            print(bcolors.FAIL + "\n Not enough MP." + bcolors.ENDC)
            continue

        player.reduceMp(spell.cost)
        enemy.takeDmg(magicDmg)
        print(bcolors.OKBLUE + "\n" + spell.name + " deals " + str(magicDmg) + " points of damage." + bcolors.ENDC)



    enemy_choice = 1
    enemyDmg = enemy.generateDmg()
    player.takeDmg(enemyDmg)
    print("Enemy attacks for " + str(enemyDmg) + " points of damage. Player HP: " + str(player.getHp()))

    print("==================")
    print("Enemy HP: " + bcolors.FAIL + str(enemy.getHp()) + "/" + str(enemy.getMaxHp()) + bcolors.ENDC)
    print("\nPlayer HP: " + bcolors.OKGREEN + str(player.getHp()) + "/" + str(player.getMaxHp()) + bcolors.ENDC)
    print("\nPlayer MP: " + bcolors.OKBLUE + str(player.getMp()) + "/" + str(player.getMaxMp()) + bcolors.ENDC + "\n")

    if enemy.getHp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.getHp() == 0:
        print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
        running = False

