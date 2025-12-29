#read input file into a list of txt lines
with open("day1_input.txt", 'r') as file:
    lines_list = file.readlines()

current_location = 50
counter = 0

def move_dial(command:str):
    global current_location, counter
    move_direction = command[0]
    move_distance = int(command[1:])

    while move_distance > 100:
        move_distance -=100

    if move_direction == "L":
        current_location -= move_distance
    elif move_direction == "R":
        current_location += move_distance
    else:
        print("Error - command not recognized")
        return
    
    if current_location > 99:
        current_location -= 100
    elif current_location < 0:
        current_location += 100

    if current_location == 0:
        counter += 1


    #print(f"direction = {move_direction}, distance = {move_distance}")
    #print(f"new location: {current_location}")


# move_dial("R44")
# move_dial("R68")
# move_dial("L20")
# move_dial("L45")

for line in lines_list:
    move_dial(line.strip())

print(counter)