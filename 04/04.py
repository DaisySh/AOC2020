#! /usr/bin/env python3
import string


def read_passports(in_file):
    passport_list = []
    with open(in_file, 'r') as f:
        f1 = f.readlines()
        t = ''
        for item in f1:
            if len(item.strip()) > 0:
                t = item.strip() + " " + t
            else:
                passport_list.append(t.strip())
                t = ''
                # print(passport_list[-1])
        # last item
        passport_list.append(t.strip())
    return passport_list


def count_pass_newline(in_file):
    with open(in_file, 'r') as f:
        f1 = f.read()
        elenco = f1.split("\n\n")
        return len(elenco)


def is_hex_str(s):
    return set(s).issubset(string.hexdigits)


def check_tag_value(tag, value):
    eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return_value = False
    if tag == 'byr':
        if len(value) == 4 and int(value) >= 1920 and int(value) <= 2002:
            return_value = True
    if tag == 'iyr':
        if len(value) == 4 and int(value) >= 2010 and int(value) <= 2020:
            return_value = True
    if tag == 'eyr':
        if len(value) == 4 and int(value) >= 2020 and int(value) <= 2030:
            return_value = True
    if tag == 'hgt':
        cm_in = value[-2:]
        if cm_in == 'cm' and int(value[:-2]) >= 150 and int(value[:-2]) <= 193:
            return_value = True
        elif cm_in == 'in' and int(value[:-2]) >= 59 and int(value[:-2]) <= 76:
            return_value = True
        else:
            return_value = False
    if tag == 'hcl':
        if value[0] == '#' and len(value[1:]) == 6 and is_hex_str(value[1:]):
            return_value = True
        else:
            return_value = False
    if tag == 'ecl':
        if len(value) == 3 and value in eye_color:
            return_value = True
    if tag == 'pid':
        return_value = len(value) == 9
    return return_value


in_file = "04/input.txt"
passport_list = read_passports(in_file)
# tags
mandatory_tags = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
ignore_tag = {'cid'}

count_ok_pass = 0
for item in passport_list:
    elem_list = item.split(' ')
    local_tags = []
    for elem in elem_list:
        elem_tag_value = elem.split(':')
        if elem_tag_value[0] != ignore_tag and check_tag_value(elem_tag_value[0], elem_tag_value[1]):
            local_tags.append(elem_tag_value[0])
    local_tags = set(local_tags)
    pass_match_tags = mandatory_tags.intersection(local_tags)
    if len(pass_match_tags) == len(mandatory_tags):
        count_ok_pass = count_ok_pass + 1
        # print(item)

print("Ok passports: ", count_ok_pass)
