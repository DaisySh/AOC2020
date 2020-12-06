#! /usr/bin/env python3

def read_groups(in_file):
    with open(in_file, 'r') as f:
        f1 = f.read()
        elenco = f1.split("\n\n")
        return elenco


def check_group(str_group):
    group_list = str_group.split('\n')
    group_answers = 0
    if len(group_list) > 1:
        all_answers = set()
        for item in group_list:
            item_set = set(item)
            if len(all_answers) == 0:
                all_answers = item_set.copy()
            else:
                all_answers = all_answers.union(item_set)
        group_answers = len(all_answers)
    else:
        item = set(group_list[0])
        group_answers = len(item)
    return group_answers


in_file = "06/input.txt"
all_groups = read_groups(in_file)
# print(all_groups)
final_count = 0
for item in all_groups:
    final_count += check_group(item)

print(final_count)
