class Weapon():
    def __init__(self, name, required_level, damage, nerfed_damage):
        self.name = name
        self.required_level = required_level
        self.damage = damage
        self.nerfed_damage = nerfed_damage

    def item_description(self):
        print(self.name)
        print("Required Level: {}".format(self.required_level))
        print("Damage Per Hit: {}".format(self.damage))
