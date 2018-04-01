import enemies
import npc
import random
import gameItems

class MapTile:
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
        It is puring down on the blue and yellow jumpsuit!
        You take it and turn it over, it reads:
        VAULT 101
        You realise that you are in Fallout 2 Universe. 
        Congradulations - now go and buy the game if you want to continue
        """

class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.80:
            self.enemy = enemies.GiantAnt()
            self.alive_text = "A giant ant toward you " \
                             "its pincers snap at you! "
            self.dead_text = "The corpse of a dead ant " \
                             "disolves on the ground. you sing "\
                             "Dead Ant, Ded Ant, Tad-Da-Da-Da"
        else: 
            self.enemy = enemies.RadScorpion()
            self.alive_text = "A giant Scorpion crols toward you " \
                             "its stinger lashes at you!"
            self.dead_text = "The corpse of a dead scorpion " \
                             "disolves on the ground. You Exclaim "\
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

class BossTile(MapTile):
    def __init__(self, x, y):
       self.enemy = enemies.Cameron()
       self.alive_text = "A man yels at you \"You Shell Not Pass\" " \
                             " and he launges at you!"
       self.dead_text = "The corpse of a dead man " \
                             "disolves on the ground. you sing "\
                             " Dead Ant, Ded Ant, Tad-Da-Da-Da"

       super().__init__(x, y)
    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".
                  format(self.enemy.damage, player.hp))

class TrapTile(MapTile):
    def __init__(self, x, y):
       self.alive_text = "You notice some strange patterns on the floor, but you barge in anyway"
       super().__init__(x, y)

    
    def intro_text(self):
        text = self.alive_text
        return text

    def modify_player(self, player):
       r = random.random()
       if r <0.5:
           self.modify_player(player)
           damage = int(random.random()*10)
           player.hp = player.hp - damage
           print("Trap does {} damage. You have {} HP remaining.".format(damage, player.hp))
       else: 
           print ("You figure that there is a trap somwhere in the room but it seam you go lucky or...")

class LootTile(MapTile): 
    def __init__(self, x, y):
        #Random Item Drop
        r = random.random()
        if r < 0.10:
            self.item = gameItems.pistol223()
            self.item_claimed = False
        else:
            self.item = gameItems.HealingPotion()
            self.item_claimed = False
        super().__init__(x, y)

    def intro_text(self):
        item = self.item
        if self.item_claimed:
            return """
            Another unremarkable part of the tample. You must forge onwards.
            """
        else:
            return """
            Someone dropped some {}.""".format(item.name)

    def modifyPlayer(self, player):
        if not self.item_claimed:
            self.item_claimed = True
            item = self.item
            player.inventory.append(item)
            print("{} added to your inventory.".format(item.name))

class PassageTile(MapTile):
    def intro_text(self):
        return """
        You are in a dark, musty temple. 
        The shadows seem to play tricks with your eyes, 
        and you can hear the faint sound of movement.
        """




#Game World Main functions
worldLocations = """
|VT|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|
|FB|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|
|PS|PS|__|__|__|LT|__|__|__|__|__|__|__|__|__|__|__|
|__|PS|PS|EN|EN|LT|__|__|__|__|__|__|__|__|__|__|__|
|__|TR|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|
|__|PS|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|
|__|PS|PS|EN|LT|__|__|__|__|__|__|__|__|__|__|__|__|
|__|EN|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|
|__|PS|PS|EN|LT|__|__|__|__|__|__|__|__|__|__|__|__|
|__|__|PS|__|__|__|__|__|__|__|__|__|__|__|__|__|__|
|__|__|TR|__|__|__|__|__|__|__|__|__|__|__|__|__|__|
|__|__|PS|PS|__|__|__|__|__|__|__|__|__|__|__|__|__|
|__|__|__|PS|PS|EN|LT|__|__|__|__|__|__|__|__|__|__|
|__|__|__|__|PS|__|EN|__|__|__|__|__|__|__|__|__|__|
|__|__|__|EN|PS|__|__|__|__|__|__|__|__|__|__|__|__|
|__|__|__|__|PS|EN|LT|__|__|__|__|__|__|__|__|__|__|
|__|__|__|__|TR|__|__|__|__|__|__|__|__|__|__|__|__|
|__|__|__|__|ST|__|__|__|__|__|__|__|__|__|__|__|__|
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
                  "EN": EnemyTile,
                  "PS": PassageTile,
                  "ST": StartTile,
                  "LT": LootTile,
                  "TR": TrapTile,
                  "__": None}


world_map = []

start_tile_location = None


def parse_world_locations():
    if not is_locations_valid(worldLocations):
        raise SyntaxError("Thi location is invalid!")

    locations_lines = worldLocations.splitlines()
    #print (locations_lines)
    locations_lines = [x for x in locations_lines if x]
    #print (len(locations_lines))
    for y, locations_row in enumerate(locations_lines):
        row = []
        locations_cells = locations_row.split("|")
        #print (locations_cells)
        locations_cells = [c for c in locations_cells if c]
        #print (len(locations_cells))
        for x, locations_cell in enumerate(locations_cells):
            #print (str(x)+":Cell: |"+locations_cell+"|")
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