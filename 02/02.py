#!/usr/bin/env python3

def count_letter(my_string, letter):
    count = 0
    for item in my_string:
        if item == letter:
            count += 1
    return count


# read file
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
        cl = count_letter(target_password, letter)
        if cl >= int(min_max[0]) and cl <= int(min_max[1]):
            correct_passwords += 1
        else:
            wrong_passwords += 1
            #print(target_password, letter, min_max[0], min_max[1])

print("OK:", correct_passwords)
print("NOP:", wrong_passwords)
