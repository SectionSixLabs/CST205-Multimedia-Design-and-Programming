class Weapon:
    def __init__(self):
        raise NotImplementedError("No we cannot make it in to the weapon")

    def __str__(self):
        return self.name

class Consumable:
    def __init__(self):
        raise NotImplementedError("No we cannot make it food")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)


