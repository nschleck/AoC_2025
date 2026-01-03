with open("day6_input.txt", 'r', newline=None) as file:
    row_list = file.readlines()

nested_list = []
for row in row_list:
    nested_list.append(row.split())

operator_row = nested_list[len(nested_list)-1]

# print(operator_row)
# for row in nested_list:
#     for item in row:
#         print(item)

grand_total = 0

for col in range(len(operator_row)):
    #print(nested_list[2][col])
    operator = operator_row[col]
    # print(col)
    if operator == '*':
        mult = 1
        for row in range(len(nested_list) - 1):
            mult *= int(nested_list[row][col])
        # print(mult)
        grand_total+= mult
    elif operator == '+':
        sum = 0
        for row in range(len(nested_list) - 1):
            sum += int(nested_list[row][col])
        # print(sum)
        grand_total+= sum
    
print(grand_total)
# print(operator_row)