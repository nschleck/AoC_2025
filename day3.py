#read input file into a list of txt lines
with open("day3_ex_input.txt", 'r') as file:
    battery_banks = file.readlines()

joltage_sum = 0

for bank in battery_banks:
    bank = bank.strip()
    #print(bank)

    digit1_maximum = 0
    digit1_position = 0
    digit2_maximum = 0

    for i in range(len(bank)-1):
        if int(bank[i]) > digit1_maximum:
            digit1_maximum = int(bank[i])
            digit1_position = i
    
    #print(f"maximum digit 1: {digit1_maximum} at position {digit1_position}")

    for j in range(digit1_position+1,len(bank)):
        if int(bank[j]) > digit2_maximum:
            digit2_maximum = int(bank[j])

    #print(f"maximum digit 2: {digit2_maximum}")
    #print(f"maximum joltage: {digit1_maximum}{digit2_maximum}")
    joltage = digit1_maximum*10+digit2_maximum
    joltage_sum += joltage

print(joltage_sum)

def get_maximum(start_index, bank_line, target_digit):
    for i in range(len(bank)-1):
        if int(bank[i]) > digit1_maximum:
            maximum = int(bank[i])
            position = i