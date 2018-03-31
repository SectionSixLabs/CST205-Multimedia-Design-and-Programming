import items


class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError("Do not create raw NPC objects.")

    def __str__(self):
        return self.name


class Toilet(NonPlayableCharacter):
    def __init__(self):
        self.name = "Toilet"
        self.gold = 100
        self.inventory = []

