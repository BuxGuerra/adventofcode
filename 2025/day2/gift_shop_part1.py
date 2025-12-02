def sum_invalid_ids(input_path):
    valid = True
    sum = 0

    with open(input_path, "r") as file:
        data = file.read()
        ranges = data.split(",")
        for r in ranges:
            ranges_in_list = r.split("-")
            min_id = int(ranges_in_list[0])
            max_id = int(ranges_in_list[1])

            for id in range(min_id, max_id+1):
                id_str = str(id)
                id_len = int(len(id_str))

                #print(id_str)
                #print(id_len)

                if id_len%2 == 1:
                    continue

                for i in range(int(id_len/2)):
                    if id_str[i] != id_str[int(id_len/2 + i)]:
                        valid = True
                        break
                    else:
                        valid = False

                if valid == False:
                    sum += id

    return sum




if __name__ == "__main__":
    input_path = "gift_shop_input.txt"
    sum = sum_invalid_ids(input_path)
    print(sum)