class Weapon:
    def __init__(self):
        raise NotImplementedError("No we cannot make it in to the weapon")

    def __str__(self):
        return self.name

class Spear(Weapon):
    def __init__(self):
        self.name = "Spear"
        self.description = "A razor tipped polearm. The shaft is wooden, and the tip is worked steel " 
        self.damage = 10

class pistol223(Weapon):
    def __init__(self):
        self.name = ".223 pistol"
        self.description = "A .223 rifle modified and cut down to a pistol. This is a one-of-a-kind firearm, obviously made with love and skill." 
        self.damage = 50
        self.rounds = 5
       
class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)


class CrustyBread(Consumable):
    def __init__(self):
        self.name = "Crusty Bread"
        self.healing_value = 10
        self.value = 12


class HealingPotion(Consumable):
    def __init__(self):
        self.name = "Healing Potion"
        self.healing_value = 50
        self.value = 60
