from characters import Character
from weapons import Weapon
import os
import random


class Warrior(Character):
    def pick_up(self, item):
        super().pick_up(item)
        if type(item) == Weapon:
            press_return = input("{} added to inventory".format(item.name))
        else:
            press_return = input("{} added to inventory".format(item))

    def check_inventory(self):
        print("\n{}'s INVENTORY\n".format(self.name))
        for i in self.inventory:
            if type(i) == Weapon:
                print(i.name)
            else:
                print(i)
        print("")


    def check_equiped_weapon(self):
        if type(self.inventory[0]) == Weapon:
            self.inventory[0].item_description()
            press_return = input("")
        else:
            press_return = input("You don't have a weapon equiped.")

    def equip_weapon(self):
        loop = False
        while loop != True:
            if os.name == 'nt':
                clear = lambda: os.system('cls')
            else:
                clear = lambda: os.system('clear')
            clear()
            print("Equipable Weapons in Inventory:\n")
            print("WEAPON NAME  <--|-->  ATTACK DAMAGE  <--|-->  LEVEL REQUIREMENT\n")
            for i in self.inventory:
                if type(i) == Weapon:
                    print("{}  <--|-->  {}  <--|-->  {}".format(i.name, i.damage, i.required_level))
            chosen_weapon = input("\nTo choose an weapon to equip, Type WEAPON NAME. Make sure you meet the level requirement!\n Type 'x' to cancel.\n")
            for i in self.inventory:
                if type(i) == Weapon:
                    if chosen_weapon.upper() == i.name:
                        self.inventory.remove(i)
                        self.inventory.insert(0, i)
                        press_return = input("You have equiped your {}".format(i.name))
                        loop = True
                        break
            if chosen_weapon.upper() == "X":
                break

    def attack(self):
        if type(self.inventory[0]) == Weapon:
            if self.inventory[0].required_level > self.level:
                return self.inventory[0].nerfed_damage
            else:
                return self.inventory[0].damage


class Monster:
    def __init__ (self, name, inventory, xp_yield, hp, damage):
        self.name = name
        self.inventory = inventory
        self.xp_yield = xp_yield
        self.hp = hp
        self.damage = damage

    def item_drop(self):
        max_index = len(self.inventory) - 1
        random_number = random.randint(0, max_index)
        return self.inventory[random_number]

    def damage_taken(self, enemy_attack, player):
        if enemy_attack == player.inventory[0].nerfed_damage:
            press_return = input("You do not meet the level requirements for this weapon!\n Your attack had it's damaged reduced!")
            press_return = input("You have done {} damage to the {}\n".format(player.inventory[0].nerfed_damage, self.name))
            self.hp -= enemy_attack
        else:
            press_return = input("You have done {} damage to the {}\n".format(player.inventory[0].damage, self.name))
            self.hp -= enemy_attack

    def attack(self):
        return self.damage
