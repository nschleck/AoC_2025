with open("day2_ex_input.txt", 'r') as file:
    input = file.read()

input_ranges = input.split(",")

id_sum = 0

for range in input_ranges:
    print(f"testing range {range}...")
    range = range.split("-")
    lower_bound = int(range[0])
    upper_bound = int(range[1])

    current = lower_bound

    while current <= upper_bound:
        id_string = str(current)
        current+=1

        if (len(id_string) % 2) != 0: #odd-number string length
            continue

        split_char = int(len(id_string) / 2)
        first_half = id_string[:split_char]
        second_half = id_string[split_char:]

        if first_half == second_half:
            id_sum += (current-1)

        

print(id_sum)