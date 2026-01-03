with open("day6_input.txt", 'r') as file:
    row_list = []
    for line in file:
        row_list.append(line.rstrip('\n'))

operator_row = row_list[len(row_list)-1]

# vert_numbers = []
grand_total = 0
mult = 0
sum = 0
operator = ''
for col, char in enumerate(operator_row):
    if char == '*' or char == '+':
        if operator == "*":
            grand_total += mult
            print(f"[ADDED] {mult} to grand_total. New sum: {grand_total}")
        elif operator == "+": 
            grand_total += sum
            print(f"[ADDED] {sum} to grand_total. New sum: {grand_total}")
    
    if char == '*':
        operator = char
        mult = 1
    elif char == "+":
        # print(sum)
        operator = char
        sum = 0    
    
    vertical_str = ''

    for row in range(len(row_list)-1):
        vertical_str += row_list[row][col]

    try:
        vertical_num = int(vertical_str)
    except:
        continue

    if operator == "*":
        mult *= vertical_num
        print(f"[multiplied] by {vertical_num}. New mult: {mult}")

    elif operator == "+":
        sum += vertical_num
        print(f"[added] {vertical_num} to sum. New sum: {sum}")

if operator == "*":
    grand_total += mult
    print(f"[ADDED] {mult} to grand_total. New sum: {grand_total}")
elif operator == "+": 
    grand_total += sum
    print(f"[ADDED] {sum} to grand_total. New sum: {grand_total}")  
    
print(grand_total)
