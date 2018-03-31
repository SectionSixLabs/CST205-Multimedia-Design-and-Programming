
class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0

class GiantAnt(Enemy):
    def __init__(self):
        self.name = "Giant Ant"
        self.hp = 10
        self.damage = 2

class RadScorpion(Enemy):
    def __init__(self):
        self.name = "Rad Scorpion"
        self.hp = 20
        self.damage = 5

class Cameron(Enemy):
    def __init__(self):
        self.name = "Cameron"
        self.hp = 80
        self.damage = 15

