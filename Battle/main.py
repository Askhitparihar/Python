from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

print("\n\n")
print("NAME                    HP                                     MP          ")
print("                        _________________________               __________ ")
print(bcolors.BOLD + "Valos:         " +
      "460/460 |" + bcolors.OKGREEN + "█                       " + bcolors.ENDC + bcolors.BOLD + "|    " +
      "65/65 |" + bcolors.OKBLUE + "██          " + bcolors.ENDC + "|")
print("                        _________________________               __________ ")
print("Grahnon:       460/460 |                         |       65/65 |          |")
print("                        _________________________               __________ ")
print("Meira:         460/460 |                         |       65/65 |          |")
print("\n\n")

# Create Black Magic
fire = Spell("Fire", 8, 80, "Black")
thunder = Spell("Thunder", 8, 160, "Black")
blizzard = Spell("Blizzard", 8, 60, "Black")
meteor = Spell("Meteor", 20, 200, "Black")
quake = Spell("Quake", 14, 140, "Black")

# Create White Magic
cure = Spell("Cure", 12, 120, "White")
cura = Spell("Cura", 18, 200, "White")

playerMagic = [fire, thunder, blizzard, meteor, cure, cura]

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
player = Person(460, 65,60, 34, playerMagic, playerItems)
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
            enemy.takeDmg(magicDmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals " + str(magicDmg) + " points of damage." + bcolors.ENDC)

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
            enemy.takeDmg(item.prop)
            print(bcolors.FAIL + "\n" + item.name + " deals " + item.prop + " points of damage." + bcolors.ENDC)


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

