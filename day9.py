import math
from itertools import combinations

class RedTile:
    all_tiles = []

    def __init__(self, coord_str:str):
        self.coords = coord_str.split(',')
        self.x = int(self.coords[0])
        self.y = int(self.coords[1])

        RedTile.all_tiles.append(self)
        # print(f"New red tile at [x:{self.x},y:{self.y}]")


# import and create red tiles list
with open("day9_input.txt", 'r') as file:
    for line in file:
        RedTile(line.rstrip('\n'))

max_area = 0
for tile_A, tile_B in combinations(RedTile.all_tiles, 2):
    area = (abs(tile_A.x - tile_B.x)+1) * (abs(tile_A.y - tile_B.y)+1)
    max_area = max(max_area, area)

print(f"Maximum area = {max_area}")