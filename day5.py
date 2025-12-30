#Read in input txt as a list of rows
with open("day5_input.txt", 'r') as file:
    row_list = file.readlines()

fresh_ID_ranges = []
available_IDs = []

for i, row in enumerate(row_list):
    row = row.strip()
    row_list[i] = row
    if "-" in row:
        fresh_ID_ranges.append(row)
    elif len(row) > 0:
        available_IDs.append(int(row))

# print(fresh_ID_ranges)
# print(available_IDs)

def is_ID_fresh(ID):
    global fresh_ID_ranges
    for ID_range in fresh_ID_ranges:
        lower_bound = int(ID_range.split("-")[0])
        upper_bound = int(ID_range.split("-")[1])
        if ID <= upper_bound and ID >= lower_bound:
            print(f"{ID} is fresh: found in range {ID_range}")
            return True
    
    print(f"{ID} is spoiled.")
    return False

def update_fresh_list(fresh_list:list, ID_range:str):
    #naive method; takes decades to evaluate with big ranges
    lower_bound = int(ID_range.split("-")[0])
    upper_bound = int(ID_range.split("-")[1])

    for ID in range(lower_bound, upper_bound+1):
        if ID not in fresh_list:
            fresh_list.append(ID)
            print(f"new fresh ID found: {ID}")
    return fresh_list

def merge_fresh_ranges(fresh_ranges:list, new_range:str):
    new_lower = int(new_range.split("-")[0])
    new_upper = int(new_range.split("-")[1])
    updated_fresh_list = []

    for eval_range in fresh_ranges:
        eval_lower = int(eval_range.split("-")[0])
        eval_upper = int(eval_range.split("-")[1])

        if (new_lower > eval_upper) or (new_upper < eval_lower):
            #no overlap
            updated_fresh_list.append(eval_range)
        else:
            #overlap => merge ranges
            new_lower = min(new_lower, eval_lower)
            new_upper = max(new_upper, eval_upper)
    
    new_range = f"{new_lower}-{new_upper}"
    updated_fresh_list.append(new_range)

    return updated_fresh_list

# merge overlapping ranges
for ID_range in fresh_ID_ranges:
    fresh_ID_ranges = merge_fresh_ranges(fresh_ID_ranges, ID_range)
print(f"new fresh list = {fresh_ID_ranges}")

#sum up ranges
sum = 0
for ID_range in fresh_ID_ranges:
    lower = int(ID_range.split("-")[0])
    upper = int(ID_range.split("-")[1])
    int_range = upper - lower + 1
    sum += int_range
print(sum)