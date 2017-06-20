from rpg_classes import Warrior
from rpg_classes import Monster
from weapons import Weapon
import os
import random

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4),
         (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5),
         (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6),
         (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7),
         (0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (9, 8),
         (0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9)

]


def get_locations():
    return random.sample(CELLS, 2)

def move_player(player, move):
    x, y = player
    if move == "LEFT: 'A'":
        x -= 1
    if move == "RIGHT 'D'":
        x += 1
    if move == "UP: 'W'":
        y -= 1
    if move == "DOWN: 'S'":
        y += 1
    return x, y

def draw_map(player, door):
    print("You: X        Door: D")
    print(" _"*10)
    tile = "|{}"
    for cell in CELLS:
        x, y = cell
        if x < 9:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            elif cell == door:
                output = tile.format("D")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            elif cell == door:
                output = tile.format("D|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)


def get_moves(player):
    moves = ["UP: 'W'", "LEFT: 'A'", "DOWN: 'S'", "RIGHT 'D'"]
    x, y = player
    if x == 0:
        moves.remove("LEFT: 'A'")
    if x == 9:
        moves.remove("RIGHT 'D'")
    if y == 0:
        moves.remove("UP: 'W'")
    if y == 9:
        moves.remove("DOWN: 'S'")
    return moves

def move_maker():
    n = True
    while n == True:
        g = input("").upper()
        n = False
        if g == "W":
            return "UP: 'W'"
        elif g == "A":
            return "LEFT: 'A'"
        elif g == "S":
            return "DOWN: 'S'"
        elif g == "D":
            return "RIGHT 'D'"
        elif g == "M":
            return "MENU"
        else:
            print("Please enter W, A, S, or D\n")
            n = True


def combat(player, monster):
    encounter = True
    while encounter:
        player_turn = True
        escape = False
        while player_turn:
            clear()
            player.show_stats()
            print("\nVS\n")
            print("Monster Type: {}".format(monster.name))
            print("HP: {}".format(monster.hp))
            print(" ")
            player_decision = input("Type one of the available moves:\n ATTACK:'A'    CONSUME POTION: 'C'    RUN: 'R'\n").upper()
            if player_decision == "A":
                monster.damage_taken(player.attack(), player)
                if player.current_hp() <= 0:
                    encounter = False
                    break
                player_turn = False
            elif player_decision == "C":
                player.consume_potion()
                player_turn = False
            elif player_decision == "R":
                coin_flip = random.randint(0,1)
                if coin_flip == 1:
                    press_return = input("You escaped!")
                    escape = True
                    player_turn = False
                    if player.current_hp() <= 0:
                        encounter = False
                        break
                else:
                    press_return = input("You couldn't run away!")
                    player.damage_received(monster.attack())
                    press_return = input("The {} has done {} damage to you!\n".format(monster.name, monster.damage))
                    if player.current_hp() <= 0:
                        encounter = False
                        break
            else:
                press_return = input("Please enter a valid move.")
        else:
            if escape == True:
                encounter = False
            elif monster.hp <= 0:
                item_dropped = monster.item_drop()
                player.level_up(monster.xp_yield)
                print("Maximum HP increased!")
                if type(item_dropped) == Weapon:
                    print("The {} dropped {}".format(monster.name, item_dropped.name))
                else:
                    print("The {} dropped {}".format(monster.name, item_dropped))
                player.pick_up(item_dropped)
                encounter = False
            else:
                player.damage_received(monster.attack())
                press_return = input("The {} has done {} damage to you!\n".format(monster.name, monster.damage))
                if player.current_hp() <= 0:
                    encounter = False


weapon1 = Weapon("WORN SHORTSWORD", 0, 10, 1)
weapon2 = Weapon("GENERIC LONGSWORD", 10, 30, 3)
weapon3 = Weapon("ELITE LONGSWORD", 20, 50, 5)
weapon4 = Weapon("LEGENDARY LONGSWORD", 30, 100, 10)


gerntling_inventory = ["poop", "poop", weapon2, "POTION", "poop"]
gernter_inventory = ["poop", "poop", weapon3, "POTION", "poop"]
gerntstrocity_inventory = ["poop", "poop", weapon4, "POTION", "poop"]
gertalopolis_prime_inventory = ["VICTORY BADGE", "VICTORY BADGE"]


game_over = False
name = input("Enter your hero's name:\n")
door_location, player_location = get_locations()
player = Warrior(name)
player.pick_up(weapon1)
player.pick_up("POTION")
level1 = True
level2 = True
level3 = True
level4 = True
victory = False
while game_over == False:
    clear()
    if victory:
        print("You are victorious! Thanks for playing!")
        break
    if player.current_hp() <= 0:
        game_over = True
    player.show_stats()
    action = input("'M' to move  |  'C' to check inventory  |  'Q' to quit\n").upper()
    if action == "M":
        while level1:
            clear()
            #ENEMYS IN LEVEL GET REFRESHED EACH LOOP
            dungeon_enemy = Monster("Gerntling", gerntling_inventory, 1, 30, 5)
            if player.current_hp() <= 0:
                break
                game_over = True
            player.show_stats()
            print("DUNGEON LEVEL 1: Gerntling Dungeon")
            draw_map(player_location, door_location)
            valid_moves = get_moves(player_location)
            print("You can move {}\nTo access Inventory/Game Menu: 'M'".format(" | ".join(valid_moves)))
            move = move_maker()
            if move == 'MENU':
                break
            if move in valid_moves:
                original_location = player_location
                player_location = move_player(player_location, move)
                if player_location == door_location:
                    if player.level < 10:
                        press_return = input("\n You need to be at least level 10 to open the stone door! Try move around and look for more {}s to fight \n".format(dungeon_enemy.name))
                        player_location = original_location
                    else:
                        level1 = False
                        door_location, player_location = get_locations()
                        press_return = input("You have survived the Gerntling Dungeon\n You open the door to the next area")
                        break
                else:
                    ambush = random.randint(0,3)
                    if ambush == 0:
                        press_return = input("A wild gerntling appears!")
                        combat(player, dungeon_enemy)
                        if player.current_hp() <= 0:
                            game_over = True
                            break
            else:
                input("\nThere's is a wall! You can't move that way!\n")
                ambush = random.randint(0,3)
                if ambush == 0:
                    press_return = input("A wild {} appears!".format(dungeon_enemy.name))
                    combat(player, dungeon_enemy)
                    if player.current_hp() <= 0:
                        game_over = True
                        break
        else:
            while level2:
                clear()
                #ENEMYS IN LEVEL GET REFRESHED EACH LOOP
                dungeon_enemy = Monster("Gernter", gernter_inventory, 2, 100, 10)
                if player.current_hp() <= 0:
                    game_over = True
                    break
                player.show_stats()
                print("DUNGEON LEVEL 2: Gernter Infested Lair")
                draw_map(player_location, door_location)
                valid_moves = get_moves(player_location)
                print("You can move {} Menu: 'M'".format(", ".join(valid_moves)))
                move = move_maker()
                if move == 'MENU':
                    break
                if move in valid_moves:
                    original_location = player_location
                    player_location = move_player(player_location, move)
                    if player_location == door_location:
                        if player.level < 20:
                            press_return = input("\n You need to be at least level 30 to open the stone door!\n Try move around and look for more {}s to fight \n".format(dungeon_enemy.name))
                            player_location = original_location
                        else:
                            level2 = False
                            door_location, player_location = get_locations()
                            press_return = input("You have survived the Gernter Infested Lair\n You open the door to the next area")
                            break
                        game_over = True
                        break
                    else:
                        ambush = random.randint(0,3)
                        if ambush == 0:
                            press_return = input("A wild {} appears!".format(dungeon_enemy.name))
                            combat(player, dungeon_enemy)
                            if player.current_hp() <= 0:
                                game_over = True
                                break
                else:
                    input("\nThere's is a wall! You can't move that way!\n")
                    ambush = random.randint(0,3)
                    if ambush == 0:
                        press_return = input("A wild gerntling appears!")
                        combat(player, dungeon_enemy)
                        if player.current_hp() <= 0:
                            game_over = True
                            break
            else:
                while level3:
                    clear()
                    #ENEMYS IN LEVEL GET REFRESHED EACH LOOP
                    dungeon_enemy = Monster("Gerntrocity", gerntstrocity_inventory, 3, 200, 20)
                    if player.current_hp() <= 0:
                        game_over = True
                        break
                    player.show_stats()
                    print("DUNGEON LEVEL 3: Domain of the Gernstrocities")
                    draw_map(player_location, door_location)
                    valid_moves = get_moves(player_location)
                    print("You can move {} Menu: 'M'".format(", ".join(valid_moves)))
                    move = move_maker()
                    if move == 'MENU':
                        break
                    if move in valid_moves:
                        original_location = player_location
                        player_location = move_player(player_location, move)
                        if player_location == door_location:
                            if player.level < 30:
                                press_return = input("\n You need to be at least level 30 to open the stone door!\n Try move around and look for more {}s to fight \n".format(dungeon_enemy.name))
                                player_location = original_location
                            else:
                                level3 = False
                                door_location, player_location = get_locations()
                                press_return = input("You have survived the Domain of the Gernstrocities\n You open the door to the next area")
                                break

                            game_over = True
                            break
                        else:
                            ambush = random.randint(0,3)
                            if ambush == 0:
                                press_return = input("A wild {} appears!".format(dungeon_enemy.name))
                                combat(player, dungeon_enemy)
                                if player.current_hp() <= 0:
                                    game_over = True
                                    break
                    else:
                        input("\nThere's is a wall! You can't move that way!\n")
                        ambush = random.randint(0,3)
                        if ambush == 0:
                            press_return = input("A wild gerntling appears!")
                            combat(player, dungeon_enemy)
                            if player.current_hp() <= 0:
                                game_over = True
                                break
                else:
                    while level4:
                        clear()
                        #ENEMYS IN LEVEL GET REFRESHED EACH LOOP
                        dungeon_enemy = dungeon_enemy = Monster("Elite Gerntrocity", gerntstrocity_inventory, 3, 200, 25)
                        dungeon_boss = Monster("Gerntalopolis Prime", gertalopolis_prime_inventory, 3, 200, 35)
                        if player.current_hp() <= 0:
                            game_over = True
                            break
                        player.show_stats()
                        print("DUNGEON LEVEL 4: Pinnacle of the Gernts")
                        draw_map(player_location, door_location)
                        valid_moves = get_moves(player_location)
                        print("You can move {} Menu: 'M'".format(", ".join(valid_moves)))
                        move = move_maker()
                        if move == 'MENU':
                            break
                        if move in valid_moves:
                            original_location = player_location
                            player_location = move_player(player_location, move)
                            if player_location == door_location:
                                if player.level < 30:
                                    press_return = input("\n You need to be at least level 30 to open the stone door!\n Try move around and look for more {}s to fight \n".format(dungeon_enemy.name))
                                    original_location = player_location
                                else:
                                    answer = input("If you open this door Gertalopolis Prime the ruler of the Gernts will be unleashed!\nDo you wish to challenge the leader of the Gernts? 'Y/N'")
                                    if answer.upper() == "Y":
                                        combat(player, dungeon_boss)
                                        if player.current_hp() <= 0:
                                            game_over = True
                                            break
                                        else:
                                            victory = True
                                            break
                                    else:
                                        player_location = original_location
                            else:
                                ambush = random.randint(0,3)
                                if ambush == 0:
                                    press_return = input("A wild {} appears!".format(dungeon_enemy.name))
                                    combat(player, dungeon_enemy)
                                    if player.current_hp() <= 0:
                                        game_over = True
                                        break
                        else:
                            input("\nThere's is a wall! You can't move that way!\n")
                            ambush = random.randint(0,3)
                            if ambush == 0:
                                press_return = input("A wild gerntling appears!")
                                combat(player, dungeon_enemy)
                                if player.current_hp() <= 0:
                                    game_over = True
                                    break
    elif action == "C":
        player.check_inventory()
        inventory_options = input("Inventory Options \n Equip Weapon: 'E' | Consume Potion 'C' | Press 'Enter' to go back\n").upper()
        if inventory_options == "E":
            player.equip_weapon()
        elif inventory_options == "C":
            player.consume_potion()

    elif action == "Q":
        press_return = input("Thanks for Playing!")
        break
    else:
        print("Please enter a valid input.")
else:
    print("You Died!\n You probably got shitty loot the whole game!\n Better luck next time!")


door_location, player_location = get_locations()
