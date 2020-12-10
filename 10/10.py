#! /usr/bin/env python3
def read_data(in_file):
    with open(in_file, 'r') as f:
        f1 = f.read()
        elenco = f1.split("\n")
        return elenco


def clean_data(in_file):
    data_list = read_data(in_file)
    for i in range(len(data_list)):
        if len(data_list[i].strip()) > 0:
            data_list[i] = int(data_list[i])
        else:
            break
    data_list = data_list[:i]
    return data_list


def check_jolts(data_list):
    # Sort ascending
    data_list.append(0)
    data_list.sort()
    i = 0
    count_diffs = {1: 0, 2: 0, 3: 1}
    print(data_list)
    while i < len(data_list):
        j = i+1
        if j >= len(data_list):
            break
        else:
            diff = data_list[j] - data_list[i]
            # print(data_list[j], data_list[i], diff)
            if diff in count_diffs.keys():
                count_diffs[diff] = count_diffs[diff] + 1
            else:
                print("AAAAAAAAAAA - ", data_list[i], data_list[j])
            i = i + 1
    print(count_diffs)
    return count_diffs, count_diffs[1] * count_diffs[3]


def count_all_combinations(data_list):
    data_list.sort()
    my_dict = {0: 1}
    for item in data_list:
        k_val = [item + 1, item + 2, item + 3]
        for k in k_val:
            if k in data_list:
                if k not in my_dict:
                    my_dict[k] = my_dict[item]
                else:
                    my_dict[k] += my_dict[item]

    # print(my_dict)
    max_value = max(my_dict.keys())
    print(my_dict[max_value])


in_file = "10/input.txt"
data_list = clean_data(in_file)

# D10.1
diffs, cj = check_jolts(data_list)
print("1s * 3s ", cj)

# D10.2
count_all_combinations(data_list)
