#read input file into a list of txt lines
with open("day3_input.txt", 'r') as file:
    battery_banks = file.readlines()

joltage_sum = 0

def get_maximum(start_index, bank_line, target_digit):
    maximum = 0
    position = 0

    final_index = len(bank_line)-target_digit

    for i in range(start_index, final_index):
        if int(bank[i]) > maximum:
            maximum = int(bank[i])
            position = i

    return maximum, position

for bank in battery_banks:
    bank = bank.strip()
    #print(bank)

    digit11_max, digit11_pos = get_maximum(0, bank, 11)
    digit10_max, digit10_pos = get_maximum(digit11_pos+1, bank, 10)
    digit9_max, digit9_pos = get_maximum(digit10_pos+1, bank, 9)
    digit8_max, digit8_pos = get_maximum(digit9_pos+1, bank, 8)
    digit7_max, digit7_pos = get_maximum(digit8_pos+1, bank, 7)
    digit6_max, digit6_pos = get_maximum(digit7_pos+1, bank, 6)
    digit5_max, digit5_pos = get_maximum(digit6_pos+1, bank, 5)
    digit4_max, digit4_pos = get_maximum(digit5_pos+1, bank, 4)
    digit3_max, digit3_pos = get_maximum(digit4_pos+1, bank, 3)
    digit2_max, digit2_pos = get_maximum(digit3_pos+1, bank, 2)
    digit1_max, digit1_pos = get_maximum(digit2_pos+1, bank, 1)
    digit0_max, digit0_pos = get_maximum(digit1_pos+1, bank, 0)

    #print(f"6 digit max: {digit5_max}{digit4_max}{digit3_max}{digit2_max}{digit1_max}{digit0_max}")

    joltage = f"{digit11_max}{digit10_max}{digit9_max}{digit8_max}{digit7_max}{digit6_max}{digit5_max}{digit4_max}{digit3_max}{digit2_max}{digit1_max}{digit0_max}"
    joltage = int(joltage)
    #print(joltage)
    #print(f"maximum digit 2: {digit2_maximum}")
    #print(f"maximum joltage: {digit1_maximum}{digit2_maximum}")
    # joltage = digit1_maximum*10+digit2_maximum
    joltage_sum += joltage

print(joltage_sum)