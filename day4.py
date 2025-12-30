#Read in input txt as a list of rows
with open("day4_input.txt", 'r') as file:
    row_list = file.readlines()
for i, row in enumerate(row_list):
    row_list[i] = row_list[i].strip()


TOTAL_ROWS = len(row_list)
TOTAL_COLUMNS = len(row_list[0])
#print(f"GRID: {TOTAL_COLUMNS}X{TOTAL_ROWS}")

def is_char_free(char, x, y):
    global TOTAL_ROWS, TOTAL_COLUMNS
    global row_list
    if char == ".":
        return

    total_obstructions = 0
    #print(f"[evaluating {x},{y}...]")

    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 and j == 0:
                continue
            if (y+i<0) or (y+i>TOTAL_ROWS-1) or (x+j<0) or (x+j>TOTAL_COLUMNS-1):
                continue
            else:
                #print(f"({x+j},{y+i})")
                test_char = row_list[y+i][x+j]
                # print(f"({x+j},{y+i})")
                # print(test_char)
                if test_char == "@":
                    total_obstructions += 1
    
    #print(f"total obstructions: {total_obstructions}")

    if total_obstructions < 4:
        return True
    else:
        return False

    
# is_char_free("@",0,0)

counter = 0
for y, row in enumerate(row_list):
    for x, char in enumerate(row):
        if is_char_free(char,x,y):
            print(f"free roll found at {x},{y}")
            counter +=1

print(counter)
