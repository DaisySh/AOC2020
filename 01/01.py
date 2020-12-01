#!/usr/bin/env python3
import random


def look_2020(u_list):
    for j in range(len(u_list)):
        i_target = random.randint(0, len(u_list))
        value_target = u_list[i_target]
        # remove value_target
        u_list.remove(value_target)
        for item in u_list:
            if (item + value_target) == 2020:
                print(item, value_target, item*value_target)
                return item, value_target
    return -1

# read file
in_list = []
with open("01/input.txt", 'r') as f:
    f1 = f.readlines()
    for item in f1:
        in_list.append(int(item.strip()))

u_list = list(set(in_list))
print(look_2020(u_list))
