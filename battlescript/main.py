from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

#Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

#WHite magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

#create some items
potion = Item("Potion", "potion", "Heals for 50", 50)
hipotion = Item("Hi-Potion","potion", "Heals for 100", 100)
superpotion = Item("Super-Potion", "potion", "Heals for 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP", 9999)
hielixer = Item("MegaElixer", "elixer","Fully restores party's HP/MP",9999)
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{"item":potion,"quantity":15},
                {"item":hipotion, "quantity":5},
                 {"item":superpotion, "quantity":5},
                 {"item":elixer,"quantity":5}, 
                 {"item":hielixer, "quantity":2},
                  {"item":grenade,"quantity":5}]



#instantiate people
player = Person(460, 65, 60, 34, player_spells, player_items)
enemy = Person(1200, 65, 45, 25,[],[])

running = True
i  = 0

print(bcolors.FAIL + bcolors.BOLD+"Enemey Attacks"+bcolors.ENDC)
while running:
    print("=======================")
    player.choose_action()
    choice = input("Choose action")
    index = int(choice)-1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for damage ",dmg,"points of damage")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose Magic"))-1
        if magic_choice == -1:
            continue
        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL+"\nNot enough MP\n"+bcolors.ENDC)
            continue

        if spell.type == "white":
        	player.heal(magic_dmg)
        	print(bcolors.OKBLUE+"\n"+spell.name+" heals for"+str(magic_dmg)+" HP"+bcolors.ENDC)
        elif spell.type == "black":
        	enemy.take_damage(magic_dmg)
        	print(bcolors.OKBLUE+"\n"+spell.name+" deals"+str(magic_dmg)+" HP"+bcolors.ENDC)
    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose Item : ")) - 1
        if item_choice == -1:
            continue
        item = player.items[item_choice]
        if item["quantity"] == 0:
            print(bcolors.OKBLUE+bcolors.BOLD+"NONE LEFT"+bcolors.ENDC)
        if item["item"].type == "potion" and item["quantity"] > 0:
            player.heal(item["item"].prop)
            item["quantity"] = item["quantity"] - 1
            print("\n"+bcolors.OKGREEN+bcolors.BOLD+item["item"].name+" Heals for "+str(item["item"].prop)+" HP"+bcolors.ENDC)
        elif item["item"].type == "elixer" and item["quantity"] > 0:
            player.hp = player.maxhp
            player.mp = player.maxmp
            item["quantity"] = item["quantity"] - 1
            print("\n"+bcolors.OKGREEN+bcolors.BOLD+item["item"].name+" fully restores HP/MP "+str(item["item"].prop)+" HP"+bcolors.ENDC)
        elif item["item"].type == "attack" and item["quantity"] > 0:
            enemy.take_damage(item["item"].prop)
            item["quantity"] = item["quantity"] - 1
            print("\n"+bcolors.FAIL+bcolors.BOLD+item["item"].name+" deals for "+str(item["item"].prop)+" points of damage"+bcolors.ENDC)
      

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for ",enemy_dmg)

    print("=================================================")
    print("ENEMY HP = ",enemy.get_hp())
    print("PLAYER HP = ",player.get_hp())

    if enemy.get_hp == 0:
        print(bcolors.OKGREEN+"YOU WIN"+bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL+"YOU ARE DEFEATED"+bcolors.ENDC)
        running = False

