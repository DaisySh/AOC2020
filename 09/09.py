#! /usr/bin/env python3
import random


def read_data(in_file):
    with open(in_file, 'r') as f:
        f1 = f.read()
        elenco = f1.split("\n")
        return elenco


def check_validity(preamble, item, random_state=True):
    for j in range(len(preamble)):
        if random_state:
            i_target = random.randint(0, len(preamble)-1)
        else:
            i_target = 0
        value_target = preamble[i_target]
        # remove value_target
        preamble.remove(value_target)
        for j in preamble:
            if (j + value_target) == item:
                # print(j, value_target, item)
                return True, j, value_target
    return False


def check_validity_seq(data, item):
    tmp_data = data.copy()
    for j in range(len(data)):
        value_target = tmp_data[0]
        tmp_data.remove(value_target)
        local_sum = 0
        for i in range(len(tmp_data)):
            local_sum += tmp_data[i]
            if local_sum == item:
                min_val = min(tmp_data[:i])
                max_val = max(tmp_data[:i])
                return True, min_val, max_val
            elif local_sum > item:
                break
    return False, -1, -1


in_file = "09/input.txt"
data_list = read_data(in_file)
# clean last row
if len(data_list[-1].strip()) == 0:
    data_list = data_list[:-1]

for i in range(len(data_list)):
    data_list[i] = int(data_list[i].strip())

idx = 0
max_idx = 25
item_not_valid = 0
for i in range(max_idx, len(data_list)):
    item = data_list[i]
    preamble = data_list[i-max_idx:i]
    if not check_validity(preamble, item):
        item_not_valid = item
        break

print("Not valid item ", item_not_valid)
valid_list = []
for item in data_list:
    if item <= item_not_valid:
        valid_list.append(item)
    else:
        break

ok_flag, min_val, max_val = check_validity_seq(valid_list, item_not_valid)
if ok_flag:
    s_tmp = "Min-Max:{}-{} Sum:{}".format(min_val, max_val, min_val+max_val)
    print(s_tmp)
