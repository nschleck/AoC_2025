import math
from itertools import combinations

class JBox:
    all_Jboxes = []
    Jbox_circuits = []

    def __init__(self, coord_str:str):
        self.coords = coord_str.split(',')
        self.x = int(self.coords[0])
        self.y = int(self.coords[1])
        self.z = int(self.coords[2])

        self.connections = [] # connected JBoxes

        JBox.all_Jboxes.append(self)
        #print(f"New Jbox at [x:{self.x},y:{self.y},z:{self.z}]")
    
    def __str__(self):
        return f"JBox at [x:{self.x},y:{self.y},z:{self.z}]"

    def calculate_distance(self, other):
        x_dist = self.x - other.x
        y_dist = self.y - other.y
        z_dist = self.z - other.z
        distance = math.sqrt(x_dist * x_dist + y_dist * y_dist + z_dist * z_dist)
        
        return distance
    
def findMinimumDistance(Jbox_list:list, prev_pairs:list):
    minimum_dist = 10000
    minimum_JBoxes = []
    for JBox_A, JBox_B in combinations(Jbox_list, 2):
        dist = JBox_A.calculate_distance(JBox_B)

        # new minimum found
        if dist < minimum_dist and [JBox_A, JBox_B] not in prev_pairs and [JBox_B, JBox_A] not in prev_pairs:
            minimum_dist = dist
            minimum_JBoxes = [JBox_A, JBox_B]
            
    prev_pairs.append(minimum_JBoxes)

    # update circuits
    for circuit in JBox.Jbox_circuits:
        if minimum_JBoxes[0] in circuit:
            circuit.append(minimum_JBoxes[1])
            break
        elif minimum_JBoxes[1] in circuit:
            circuit.append(minimum_JBoxes[0])   
            break 

    return minimum_dist, minimum_JBoxes, prev_pairs

# import and create J Boxes
with open("day8_ex_input.txt", 'r') as file:
    for line in file:
        JBox(line.rstrip('\n'))


# find minimum Jbox distance
distance_pairs = []
for i in range(2):
    min_d, boxes, pairs = findMinimumDistance(JBox.all_Jboxes , distance_pairs)

    print(f"~~~~ Loop {i} ~~~~")
    print(f"minimum distance: {min_d}")
    print(boxes[0])
    print(boxes[1])
    print()
