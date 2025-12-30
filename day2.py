with open("day2_input.txt", 'r') as file:
    input = file.read()

input_ranges = input.split(",")

id_sum = 0

for sample_range in input_ranges:
    print(f"[testing range {sample_range}...]")
    sample_range = sample_range.split("-")
    lower_bound = int(sample_range[0])
    upper_bound = int(sample_range[1])

    current = lower_bound

    while current <= upper_bound:
        id_string = str(current)
        current += 1

        for substring_length in range(1, (len(id_string))):
            valid_ID = False
            if (len(id_string) % substring_length) != 0: # no even division
                continue

            substring_list = []

            for i in range(0, len(id_string),substring_length):
                substring_list.append(id_string[i:i+substring_length])

            #print(substring_list)

            test_element = substring_list[0]
            for element in substring_list:
                if element != test_element:
                    #print(f"\tvalid ID substrings")
                    valid_ID = True
                    break

            if not valid_ID:
                id_sum += (current-1)
                print(f"\t- invalid ID found: {current-1}")
                break

    
print(f"Final Sum: {id_sum}")