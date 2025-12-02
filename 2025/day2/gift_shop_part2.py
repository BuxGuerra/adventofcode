def sum_invalid_ids(input_path):
    valid = True
    sum = 0

    with open(input_path, "r") as file:
        data = file.read()
        ranges = data.split(",")

        # Iterate through ranges
        for r in ranges:
            ranges_in_list = r.split("-")
            min_id = int(ranges_in_list[0])
            max_id = int(ranges_in_list[1])

            # Iterate through ids in range
            for id in range(min_id, max_id+1):
                id_str = str(id)
                id_len = int(len(id_str))

                # Iterate through possible group sizes
                for i in range(1,id_len):
                    if id_len%(i) != 0:
                        continue

                    parts = []
                    j = 0

                    # Split id into equal parts of size i
                    while j<id_len:
                        parts.append(id_str[j:j+i])
                        j = j+i

                    # Check all parts in division are equal (invalid id) or not
                    valid = False
                    for j in range(len(parts)-1):
                        if parts[j] != parts[j+1]:
                            valid = True
                        
                    if valid == False:
                        sum += id
                        break

    return sum




if __name__ == "__main__":
    input_path = "gift_shop_input.txt"
    sum = sum_invalid_ids(input_path)
    print(sum)