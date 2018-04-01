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
            self.alive_text ="""
                             A giant ant toward you 
                             its pincers snap at you! """
            self.dead_text = """
                             The corpse of a dead ant 
                             disolves on the ground. you sing
                             Dead Ant, Ded Ant, Tad-Da-Da-Da"""
        else: 
            self.enemy = enemies.RadScorpion()
            self.alive_text = """
                             A giant Scorpion crols toward you 
                             its stinger lashes at you!"""
            self.dead_text = """
                             The corpse of a dead scorpion 
                             disolves on the ground. You Exclaim 
                             Whisky Tango Foxtrot was that thing?"""

        super().__init__(x, y)
    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("""
                  Enemy does {} damage. You have {} HP remaining.
                  """.format(self.enemy.damage, player.hp))

class BossTile(MapTile):
    def __init__(self, x, y):
       self.enemy = enemies.Cameron()
       self.alive_text = """
                  A man yels at you:            
                  My Name is {}!!!
                  "You Shell Not Pass" and launges at you!
                  """.format(self.enemy.name)
       self.dead_text = """
                  The corpse of a dead man disolves on the ground. you sing
                      Dead Ant, Ded Ant, Tad-Da-Da-Da"""

       super().__init__(x, y)
    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("""
                  Enemy does {} damage. You have {} HP remaining.
                  """.
                  format(self.enemy.damage, player.hp))

class TrapTile(MapTile):
    def __init__(self, x, y):
       self.alive_text = """
                         You notice some strange patterns on the floor, but you barge in anyway
                         """
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
           print("""
                 Trap does {} damage. You have {} HP remaining.
                 """.format(damage, player.hp))
       else: 
           print ("""
                 You figure that there is a trap somwhere in the room but it seam you go lucky or...
                 """)

class LootTile(MapTile): 
    def __init__(self, x, y):
        #Random Item Drop
        r = random.random()
        if r < 0.10:
            self.item = gameItems.pistol223()
            self.item_claimed = False
        elif r < 0.80:
            self.item = gameItems.HealingPouder()
            self.item_claimed = False
        else: 
            self.item = gameItems.pistol223()
            self.item_claimed = True
        super().__init__(x, y)

    def intro_text(self):
        if self.item_claimed:
            return """
            Another unremarkable part of the tample. You must forge onwards.
            """
        else:
            return """
            Someone dropped some {}.""".format(self.item.name)

    def modifyPlayer(self, player):
        if not self.item_claimed:
            self.item_claimed = True
            item = self.item
            player.inventory.append(item)
            print("{} added to your inventory.".format(item.name))

class PassageTile(MapTile):
    def intro_text(self):
        roomDesc = ["""
        You are in a dark, musty temple. 
        The shadows seem to play tricks with your eyes, 
        and you can hear the faint sound of movement.
        ""","""
        You see a coridor draped in darkness in front of you
        What does this darknes holds for you? 
        ""","""
        You see skatered pieces of cealing on the flor. 
        Watch your steps.
        ""","""
        You can see body lying on the floor, you get closer. 
        Name tag reads "Parzeval" 
        You find the bloody message close to the corps. 
        BeWare they are working for IOI,  they are sixers!
        Don't trust them!
        ""","""
        You start seeing strang glowing symbols in the dark. 
        Sudenly you relise what they are saying: 
        Peace of Eden belongs to us!
        ""","""
        On the walls you can read the big sign: 
        "Save Chear Leader - Save the World"
        ""","""
        A crack in the ceiling above the middle of the north wall 
        allows a trickle of water to flow down to the floor. 
        The water pools near the base of the wall, 
        and a rivulet runs along the wall an out into the hall. 
        The water smells fresh
        ""","""
        A large arched niche pierces one wall of this chamber. 
        Filled with rotting wood and rubble the niche appears 
        to be a dumping ground of sorts. Elsewhere in the room, 
        several sections of floor are cracked and pitted.
        """, """
        This irregularly-shaped room has an uneven floor. 
        Several small puddles have gathered in the deeper depressions. 
        Elsewhere, small pieces of rubble litter the floor.
        ""","""
        The arched ceiling of this chamber rises to a height of 20 ft. 
        In the centre of the room, but is barely man-high where it meets the walls.
        The arches holding the ceiling aloft are carved to represent writhing tentacles;
        a few have been defaced but the upper portions of all remain untouched.
        ""","""
        A pile of rotting wood, rubbish and other detritus partially obscures one wall of this chamber.
        Clearly used as a rubbish dump, the stench of decay and rot hangs heavily in the air
        ""","""
        This large chamber was the scene of an ancient battle. 
        Skeletal remains of at least a dozen humanoids lie scattered about the room where they fell. 
        Several rusting broken spears and shattered, rotting shields lie among the fallen.
        ""","""
        Part of one wall of this room has collapsed, revealing the natural rock behind the dressed stone wall. 
        The rubble has been moved to create a breastwork across one of the room’s exits. 
        Splatters of old, dried blood decorate the top of the breastwork.
        ""","""
        The remains of a cold camp are evident here. 
        A tattered cloak—sized for a gnome or halfling—along with two empty wineskins and the stripped bones
        of a chicken and crusts of mouldy bread bear testimony to an explorer’s rest.
        ""","""
        A gaping open pit in one of this chamber’s doorways blocks access to the area beyond. 
        Two skeletons, pierced by dozens of tiny stone spikes, lie in the pit. 
        The chamber beyond boasts a stone plinth and altar set in a semi-circular niche. 
        The chamber’s other doorway—twice the width of the trapped one—appears unprotected.
        """]
        
        print (self.x, self.y)
        roomDesc= random.choice(roomDesc)
        print (roomDesc)
        if tile_at(self.x, self.y - 1):
            print("""You can see passage to the north
            """)
        if tile_at(self.x, self.y + 1):
            print("""You can see passage to the south
            """)
        if tile_at(self.x + 1, self.y):
            print("""You can see passage to the east
            """)
        if tile_at(self.x - 1, self.y):
            print("""You can see passage to the west
            """)
        return ""




#Game World Main functions
worldLocations = """
|VT|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|
|FB|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|
|PS|LT|__|__|__|LT|__|__|__|__|__|__|__|__|__|__|__|
|__|PS|EN|LT|EN|LT|__|__|__|__|__|__|__|__|__|__|__|
|__|TR|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|
|__|PS|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|
|__|LT|PS|EN|LT|__|__|__|__|__|__|__|__|__|__|__|__|
|__|EN|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|
|__|PS|TR|EN|LT|__|__|__|__|__|__|__|__|__|__|__|__|
|__|__|PS|__|__|__|__|__|__|__|__|__|__|__|__|__|__|
|__|__|TR|__|__|__|__|__|__|__|__|__|__|__|__|__|__|
|__|__|EN|PS|__|__|LT|__|__|__|__|__|__|__|__|__|__|
|__|__|__|TR|EN|EN|LT|__|__|__|__|__|__|__|__|__|__|
|__|__|__|__|PS|__|EN|LT|__|__|__|__|__|__|__|__|__|
|__|__|__|__|TR|__|__|__|__|__|__|__|__|__|__|__|__|
|__|__|LT|EN|PS|__|EN|LT|__|__|__|__|__|__|__|__|__|
|__|__|__|__|PS|EN|LT|__|__|__|__|__|__|__|__|__|__|
|__|__|__|__|PS|__|__|__|__|__|__|__|__|__|__|__|__|
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