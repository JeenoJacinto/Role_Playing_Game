class Character:
    def __init__ (self, name, **kwargs):
        self.name = name
        self.inventory = []
        self.level = 1
        self.max_hp = 30
        self.damage_taken = 0
        for key, value in kwargs.items():
            setattr(self, key, value)

    def damage_received(self, enemy_attack):
        self.damage_taken += enemy_attack

    def consume_potion(self):
        if "POTION" in self.inventory:
            self.inventory.remove("POTION")
            self.damage_taken -= int(self.max_hp / 2)
            if self.damage_taken < 0:
                self.damage_taken = 0
            press_return = input("You have consumed one of your POTIONS")
        else:
            press_return = input("You have ran out of POTIONS!")

    def current_hp(self):
        current_hp = self.max_hp - self.damage_taken
        return current_hp

    def show_stats(self):
        print("Name: {}".format(self.name))
        print("Level: {}".format(self.level))
        print("HP: {}/{}".format(self.current_hp(), self.max_hp))
        print("Equiped Weapon: {}".format(self.inventory[0].name))

    def pick_up(self, item):
        self.inventory.append(item)

    def level_up(self, amount):
        self.level += amount
        self.max_hp += amount * 5
        press_return = input("You have gained experienced! Your new level is {}!".format(self.level))
    def set_level(self, desired_level):
        self.level = desired_level
