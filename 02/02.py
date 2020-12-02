#!/usr/bin/env python3

def count_letter(my_string, letter):
    count = 0
    for item in my_string:
        if item == letter:
            count += 1
    return count


def check_position(my_string, letter, min_max):
    min_value = int(min_max[0]) - 1
    max_value = int(min_max[-1]) - 1
    if (my_string[min_value] == letter) ^ (my_string[max_value] == letter):
        return True
    return False


count_flag = False
correct_passwords = 0
wrong_passwords = 0
with open("02/input.txt", 'r') as f:
    f1 = f.readlines()
    for item in f1:
        tmp_item = item.strip()
        tmp_sep = tmp_item.split(':')
        target_password = tmp_sep[-1].strip()
        target_rule = tmp_sep[0].split(' ')
        min_max = target_rule[0].split('-')
        letter = target_rule[-1]
        ok_flag = False
        if count_flag:
            cl = count_letter(target_password, letter)
            ok_flag = cl >= int(min_max[0]) and cl <= int(min_max[1])
        else:
            ok_flag = check_position(target_password, letter, min_max)

        if ok_flag:
            correct_passwords += 1
        else:
            wrong_passwords += 1

if count_flag:
    print('Min-Max frequency')
else:
    print('Min-Max indexing')

print("OK:", correct_passwords)
print("NOP:", wrong_passwords)
