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
    minimum_dist = 1000000
    minimum_JBoxes = []
    for JBox_A, JBox_B in combinations(Jbox_list, 2):
        dist = JBox_A.calculate_distance(JBox_B)

        # new minimum found
        if dist < minimum_dist and [JBox_A, JBox_B] not in prev_pairs and [JBox_B, JBox_A] not in prev_pairs:
            minimum_dist = dist
            minimum_JBoxes = [JBox_A, JBox_B]
            
    prev_pairs.append(minimum_JBoxes)

    # update circuits
    new_circuit = True
    for circuit in JBox.Jbox_circuits:
        if minimum_JBoxes[0] in circuit:
            circuit.append(minimum_JBoxes[1])
            new_circuit = False
            break
        elif minimum_JBoxes[1] in circuit:
            circuit.append(minimum_JBoxes[0])
            new_circuit = False   
            break 
    if new_circuit:
        JBox.Jbox_circuits.append([minimum_JBoxes[0], minimum_JBoxes[1]])

    return minimum_dist, minimum_JBoxes, prev_pairs

def sortPairsByMinDist(Jbox_list:list):
    Jbox_pairs = []
    for JBox_A, JBox_B in combinations(Jbox_list, 2):
        dist = JBox_A.calculate_distance(JBox_B)
        Jbox_pairs.append([dist, JBox_A, JBox_B])

    sorted_pairs = sorted(Jbox_pairs, reverse=False)
    # for pair in sorted_pairs:
    #     print(f"Dist: {pair[0]}, {pair[1]}, {pair[2]}")
    print(len(sorted_pairs))

    return sorted_pairs


# import and create J Boxes
with open("day8_ex_input.txt", 'r') as file:
    for line in file:
        JBox(line.rstrip('\n'))

# create pairs list, sorted by distance
sorted_Jbox_pairs = sortPairsByMinDist(JBox.all_Jboxes)

# Update circuits
for i in range(10):
    #print(f"~~~~ Loop {i} ~~~~")
    JBox_A = sorted_Jbox_pairs[i][1]
    JBox_B = sorted_Jbox_pairs[i][2]
    new_circuit = True

    # TODO handle connecting 2 existing circuits
    for circuit in JBox.Jbox_circuits:
        if JBox_A in circuit:
            circuit.append(JBox_A)
            new_circuit = False
            # print(circuit)
            break
        elif JBox_B in circuit:
            circuit.append(JBox_B)
            new_circuit = False 
            # print(circuit)  
            break 
    if new_circuit:
        JBox.Jbox_circuits.append([JBox_A, JBox_B])
        # print([JBox_A, JBox_B])


# find longest circuits
# sorted_circuits = sorted(JBox.Jbox_circuits, key=len, reverse=True)
# print(len(sorted_circuits[0]))
# print(len(sorted_circuits[1]))
# print(len(sorted_circuits[2]))
# print(f"final: {len(sorted_circuits[0])*len(sorted_circuits[1])*len(sorted_circuits[2])}")