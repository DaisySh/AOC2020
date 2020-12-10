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
    return count_diffs[1] * count_diffs[3]


in_file = "10/input.txt"
data_list = clean_data(in_file)
# D10.1
cj = check_jolts(data_list)
print("1s * 3s ", cj)
