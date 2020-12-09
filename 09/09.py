#! /usr/bin/env python3
import random


def read_data(in_file):
    with open(in_file, 'r') as f:
        f1 = f.read()
        elenco = f1.split("\n")
        return elenco


def check_validity(preamble, item):
    for j in range(len(preamble)):
        i_target = random.randint(0, len(preamble)-1)
        value_target = preamble[i_target]
        # remove value_target
        preamble.remove(value_target)
        for j in preamble:
            if (j + value_target) == item:
                # print(j, value_target, item)
                return True
    return False


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
