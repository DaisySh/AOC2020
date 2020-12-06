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


def check_yes_frequency(str_group):
    group_list = str_group.split('\n')
    group_answers = 0
    if len(group_list) > 1:
        all_answers = set()
        for item in group_list:
            item_set = set(item)
            all_answers = all_answers.union(item_set)
        for answer in all_answers:
            count_answer = 0
            for item in group_list:
                if answer in set(item):
                    count_answer += 1
            if count_answer == len(group_list):
                group_answers += 1
    else:
        group_answers = len(group_list[0])
    # print(str_group, group_answers)
    return group_answers


in_file = "06/input.txt"
all_groups = read_groups(in_file)
# print(all_groups)
yes_final_count = 0
shared_final_count = 0
for item in all_groups:
    item = item.strip()
    yes_final_count += check_group(item)
    shared_final_count += check_yes_frequency(item)

print('Count yes:', yes_final_count)
print('Count shared yes:', shared_final_count)
