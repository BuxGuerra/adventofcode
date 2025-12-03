def calculate_max_joltage_bank(line):
    max = [0 for i in range(12)]
    index = [0 for i in range(12)]

    for i in range(12):
        if i == 0:
            last_index = -1
        else:
            last_index = index[i-1]

        for j in range(last_index+1, len(line)-(12-i)):
            if int(line[j]) > max[i]:
                max[i] = int(line[j])
                index[i] = j

    result = 0
    for k in range(12):
        result += max[11 - k] * (10**k)

    return result



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