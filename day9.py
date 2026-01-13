import math
from itertools import combinations

class RedTile:
    all_tiles = []
    maximum_X = 0
    maximum_Y = 0

    def __init__(self, coord_str:str):
        self.coords = coord_str.split(',')
        self.x = int(self.coords[0])
        self.y = int(self.coords[1])

        RedTile.all_tiles.append(self)
        RedTile.maximum_X = max(RedTile.maximum_X, self.x)
        RedTile.maximum_Y = max(RedTile.maximum_Y, self.y)
        # print(f"New red tile at [x:{self.x},y:{self.y}]")
    
    def __str__(self):
        return f"[{self.x}, {self.y}]"

def findMaxRectangle():
    max_area = 0
    for tile_A, tile_B in combinations(RedTile.all_tiles, 2):
        area = (abs(tile_A.x - tile_B.x)+1) * (abs(tile_A.y - tile_B.y)+1)
        max_area = max(max_area, area)
    print(f"Maximum area = {max_area}")

def connectGraphicRedTiles(tile:RedTile, prev_tile:RedTile, graphic):
    col = tile.x
    row = tile.y

    if (tile.y == prev_tile.y): # Same Row
        #print(f"Connecting Horiz: {prev_tile} to {tile}")
        prev_row_str = graphic[row]
        green_tile_count = abs(tile.x - prev_tile.x)-1
        green_tiles = ""
        for j in range(green_tile_count):
            green_tiles += "X"
        
        graphic[row] = prev_row_str[:min(col, prev_tile.x)] + "#" + green_tiles + "#" + prev_row_str[max(col, prev_tile.x)+1:]

    else: # Same Column
        #print(f"Connecting Vert: {prev_tile} to {tile}")
        graphic[prev_tile.y] = graphic[prev_tile.y][:col] + "#" + graphic[prev_tile.y][col+1:]
        graphic[row] = graphic[row][:col] + "#" + graphic[row][col+1:]

        start_row_index = min(prev_tile.y, row)+1
        #print(f"\tStart index: {start_row_index}; rows: {abs(prev_tile.y - row)-1}")
        for j in range(start_row_index, start_row_index + abs(prev_tile.y - row)-1):
            #print(f"\tAdding green tile to row {j}")
            graphic[j] = graphic[j][:col] + "X" + graphic[j][col+1:]
    
    return graphic

def printGraphic(matrix:list):
    for row in matrix:
        print(row)
    print()

def buildGraphicMatrix():
    # Make initial matrix
    graphic = []
    for row in range(RedTile.maximum_Y+2):
        row_str = ""
        for col in range(RedTile.maximum_X+3):
            row_str += "."
        graphic.append(row_str)
        #print(row_str)

    #Add red and green tiles to graphic
    for i in range(1,len(RedTile.all_tiles)):
        print(f"~~~~~ Loop {i} ~~~~~")
        printGraphic(graphic)
        tile = RedTile.all_tiles[i]
        prev_tile = RedTile.all_tiles[i-1]
        graphic = connectGraphicRedTiles(tile, prev_tile, graphic)

    printGraphic(graphic)
    graphic = connectGraphicRedTiles(RedTile.all_tiles[0], RedTile.all_tiles[-1], graphic)

    return graphic

# import and create red tiles list
with open("day9_ex_input.txt", 'r') as file:
    for line in file:
        RedTile(line.rstrip('\n'))

matrix = buildGraphicMatrix()
printGraphic(matrix)