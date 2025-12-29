#read input file into a list of txt lines
with open("day1_input.txt", 'r') as file:
    lines_list = file.readlines()

current_location = 50
counter = 0

def move_dial(command:str):
    global current_location, counter
    move_direction = command[0]
    move_distance = int(command[1:])

    # while move_distance > 100:
    #     move_distance -=100

    if current_location == 0:
        counter -= 1

    if move_direction == "L":
        current_location -= move_distance
    elif move_direction == "R":
        current_location += move_distance
    else:
        print("Error - command not recognized")
        return
    
    # print(f"command direction = {move_direction}, distance = {move_distance}")
    # print(f"new location: {current_location}")

    if current_location == 0:
        counter += 1
        # print(f"current location: 0; counter: {counter}")

    while current_location > 99:
        current_location -= 100
        counter += 1
        # print(f"new location: {current_location}, passed 0; counter: {counter}")


    while current_location < 0:
        current_location += 100
        counter += 1
        # print(f"new location: {current_location}, passed 0; counter: {counter}")

def move_dial_v2(command:str):
    global current_location, counter
    move_direction = command[0]
    move_distance = int(command[1:])

    if move_direction == "L":
        while move_distance > 0:
            current_location -= 1
            move_distance -= 1

            if current_location == 0:
                counter+=1
            elif current_location < 0:
                current_location += 100

    elif move_direction == "R":
        while move_distance > 0:
            current_location += 1
            move_distance -= 1
            
            if current_location == 100:
                counter+=1
                current_location -= 100


    else:
        print("Error - command not recognized")
        return


for line in lines_list:
    move_dial_v2(line.strip())

print(f"final counter: {counter}")