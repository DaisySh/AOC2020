#! /usr/bin/env python3

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
        if elem_tag_value[0] != ignore_tag:
            local_tags.append(elem_tag_value[0])
    local_tags = set(local_tags)
    pass_match_tags = mandatory_tags.intersection(local_tags)
    if len(pass_match_tags) == len(mandatory_tags):
        count_ok_pass = count_ok_pass + 1
        # print(item)

print("Ok passports: ", count_ok_pass)
