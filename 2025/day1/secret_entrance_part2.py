def get_password(input_path):
    start_postition = 50
    actual_position = start_postition
    number_of_zeros = 0

    with open(input_path, "r") as file:
        for line in file:
            direction = line[0]
            distance = int(line[1:])

            while distance >= 100:
                number_of_zeros += 1
                distance = distance - 100

            if direction == "R":
                actual_position = (actual_position + distance)
                if actual_position >= 100:
                    number_of_zeros += 1
                    actual_position = actual_position % 100

            if direction == "L":
                if actual_position == 0:
                    actual_position = (actual_position - distance)
                    actual_position = 100 + actual_position
                else:
                    actual_position = (actual_position - distance)
                    if actual_position < 0:
                        number_of_zeros += 1
                        actual_position = 100 + actual_position
                    elif actual_position == 0:
                        number_of_zeros += 1

            print("Number of zeros: " + str(number_of_zeros) + " Position: " + str(actual_position))

    return number_of_zeros

    



if __name__ == "__main__":
    input_path = "secret_entrance_input.txt"
    password = get_password(input_path)
    print(password)