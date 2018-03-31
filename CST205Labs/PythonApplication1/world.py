import enemies
import npc
import random

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
        You find yourself in a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """

worldLocations = """
|EN|EN|VT|EN|EN|
|EN|  |  |  |EN|
|EN|FC|EN|  |TT|
|TT|  |ST|FC|EN|
|FC|  |EN|  |FC|
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
                  "EN": EnemyTile,
                  "ST": StartTile,
                  "FC": FindCupsTile,
                  "TT": ToiletTile,
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