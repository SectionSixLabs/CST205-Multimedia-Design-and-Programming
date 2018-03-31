import enemies
import npc
import random
import gameItems

class MapTitle:
    """description of class"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass

class StartTile(MapTile):
    def intro_text(self):
        return """
        You find yourself at the entrance of a temple.
        You look around and find that only path you have is to go inside,
        as other paths are blocked by the palicade and sharpened stakes.   
        """
class VictoryTile(MapTile):
    def modify_player(self, player):
        player.victory = True

    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
        Victory is yours!
        """

class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.GiantAnt()
            self.alive_text = "A giant ant toward you " \
                             "its pincers snap at you!"
            self.dead_text = "The corpse of a dead ant " \
                             "disolves on the ground. you sing"\
                             "Dead Ant, Ded Ant, Tad-Da-Da-Da"
        else: 
            self.enemy = enemies.RadScorpion()
            self.alive_text = "A giant Scorpion crols toward you " \
                             "its stinger lashes at you!"
            self.dead_text = "The corpse of a dead scorpion " \
                             "disolves on the ground. You Exclaim"\
                             "Whisky Tango Foxtrot was that thing? "

        super().__init__(x, y)
    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".
                  format(self.enemy.damage, player.hp))


class LootTile(MapTitle): 
    def __init__(self, x, y):
        #Random Item Drop
        r = random.random()
        if r < 0.10:
            self.item = gameItems.pistol223
            self.item_claimed = False
        elif r < 0.80:
            self.item = gameItems.HealingPowder
            self.item_claimed = False
        else:
            self.item = gameItems.Antidote
            self.item_claimed = False
        super().__init__(x, y)

    def modifyPlayer(self, player):
        if not self.item_claimed:
            self.item_claimed = True
            inventory.append(self.item)
            print("{} added to your inventory.".format(self.item))


#Game World Main functions
worldLocations = """
|VT|  |  |  |  |  |  | 
|FB|  |  |  |  |  |  | 
|DT|PS|  |  |  |LT|  | 
|  |PS|PS|EN|EN|LT|  | 
|  |TR|  |  |  |  |  | 
|  |DT|  |  |  |  |  | 
|  |PS|PS|EN|LT|  |  | 
|  |EN|  |  |  |  |  | 
|  |PS|PS|EN|LT|  |  | 
|  |  |PS|  |  |  |  | 
|  |  |TR|  |  |  |  | 
|  |  |DT|PS|  |  |  | 
|  |  |  |PS|PS|EA|LT|
|  |  |  |  |PS|  |EA|
|  |  |  |EA|PS|  |  |
|  |  |  |  |PS|EA|LT|
|  |  |  |  |EA|  |  |
|  |  |  |  |ST|  |  |
"""


def is_locations_valid(locations):
    if locations.count("|ST|") != 1:
        return False
    if locations.count("|VT|") == 0:
        return False
    lines = locations.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True

tile_type_dict = {"VT": VictoryTile,
                  "FB": BossTile,
                  "EA": EnemyAnt,
                  "PS": Passage,
                  "ST": StartTile,
                  "LT": LootTile,
                  "TR": TrapTile,
                  "  ": None}


world_map = []

start_tile_location = None


def parse_world_locations():
    if not is_locations_valid(worldLocations):
        raise SyntaxError("Thi location is invalid!")

    locations_lines = worldLocations.splitlines()
    locations_lines = [x for x in locations_lines if x]

    for y, locations_row in enumerate(locations_lines):
        row = []
        locations_cells = locations_row.split("|")
        locations_cells = [c for c in locations_cells if c]
        for x, locations_cell in enumerate(locations_cells):
            tile_type = tile_type_dict[locations_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)

        world_map.append(row)


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None