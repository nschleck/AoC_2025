with open("day7_input.txt", 'r') as file:
    row_list = []
    for line in file:
        row_list.append(line.rstrip('\n'))


count = 0
row_str = row_list[0]
next_row_str = row_list[1]

print(row_str)

for row in range(1, len(row_list)):
    for col, char in enumerate(row_str):
        if char == "S" or char == "|":
            next_char = next_row_str[col]
            if next_char == "^":
                next_row_str = next_row_str[:col-1] + "|^|" + next_row_str[col+2:]  
                count += 1  
            else:
                # insert a "|" char below
                next_row_str = next_row_str[:col] + "|" + next_row_str[col+1:]    
            # print(f"^ found at row {row}, column {col}")
    
    print(f"{next_row_str}   [row {row}]")
    row_str = next_row_str
    try:
        next_row_str = row_list[row+1]
    except IndexError:
        pass

#print(next_row_str)

print(count)