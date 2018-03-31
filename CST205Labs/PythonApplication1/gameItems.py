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
        raise NotImplementedError("No we cannot make it food")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)

class HealingPowder(Consumable):
    def __init__(self):
         self.name = "Healing Powder"
         self.description = "A very powerful healing magic- though it will bring the feeling of sleep to your head."
         self.healing_value = 50

class Antidote(Consumable):
    def __init__(self):
         self.name = "Antidote"
         self.description = "A bottle containing a home-brewed antidote for poison. A milky solution with floating pieces of radscorpion flesh"
         self.healing_value = 25