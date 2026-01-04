import random
with open("day7_input.txt", 'r') as file:
    row_list = []
    for line in file:
        row_list.append(line.rstrip('\n'))


row_str = row_list[0]
next_row_str = row_list[1]

# create paths list and a blank path template
paths_list = []
paths_row = []
for i in range(len(row_str)):
    paths_row.append(0)
for i, char in enumerate(row_str):
    if char == "S":
        paths_row[i] = 1

next_paths_row = paths_row.copy()

# print(f"{row_str}   {paths_row}")

for row in range(1, len(row_list)):
    for col, char in enumerate(row_str):
        if char == "S" or char == "|":
            next_char = next_row_str[col]
            if next_char == "^":
                next_row_str = next_row_str[:col-1] + "|^|" + next_row_str[col+2:]  
                next_paths_row[col-1] += paths_row[col]
                next_paths_row[col+1] += paths_row[col]
                next_paths_row[col] = 0
            else:
                # insert a "|" char below
                next_row_str = next_row_str[:col] + "|" + next_row_str[col+1:]    
                # next_paths_row[col] += paths_row[col] #max(paths_row[col],1)
            # print(f"^ found at row {row}, column {col}")
    
    #sum up paths
    sum = 0
    for item in next_paths_row:
        sum+=item

    print(f"{row_str}   {next_paths_row} [row {row}] [{sum} paths]")

    row_str = next_row_str
    paths_row = next_paths_row.copy()
    try:
        next_row_str = row_list[row+1]
    except IndexError:
        pass

print(f"{row_str}   {paths_row} [row {row}]")

