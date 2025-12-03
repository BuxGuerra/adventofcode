def calculate_max_joltage_bank(line):
    max1 = 0
    index_max1 = 0
    max2 = 0
    for i in range(len(line)-2):
        if int(line[i]) > max1:
            max1= int(line[i])
            index_max1 = i

    for j in range(index_max1+1, len(line)-1):
        if int(line[j]) > max2:
            max2= int(line[j])

    return max2 + 10*max1


def calculate_maximum_sum_joltages(input_path):
    total_joltage = 0
    with open(input_path, "r") as file:
        for line in file:
            max_joltage_bank = calculate_max_joltage_bank(line)
            total_joltage += max_joltage_bank

    return total_joltage


if __name__ == "__main__":
    input_path = "lobby_input.txt"
    max_joltage = calculate_maximum_sum_joltages(input_path)
    print(max_joltage)