#! /usr/bin/env python3

def read_boot(in_file):
    with open(in_file, 'r') as f:
        f1 = f.read()
        elenco = f1.split("\n")
        return elenco


def get_instruction(i_str):
    i_instruction, s_item = i_str.split(' ')
    i_simbol = s_item[0]
    i_number = int(s_item[1:])
    return i_instruction, i_simbol, i_number


# in_file = '08/input2.txt'
in_file = '08/input.txt'

my_boot = read_boot(in_file)
# clean last row
if len(my_boot[-1].strip()) == 0:
    my_boot = my_boot[:-2]

access_flag = [False for item in my_boot]
i = 0
acc = 0
while i < len(my_boot):
    i_item = my_boot[i].strip()
    i_instruction, i_simbol, i_number = get_instruction(i_item)
    if not access_flag[i]:
        access_flag[i] = True
        if i_instruction == 'nop':
            i += 1
        elif i_instruction == 'acc':
            t = "{} {} {}".format(acc, i_simbol, i_number)
            print(t)
            acc = eval(t)
            i += 1
        elif i_instruction == 'jmp':
            t = "{} {} {}".format(i, i_simbol, i_number)
            print(t)
            i = eval(t)
    else:
        break

print('Acc at first repetition:', acc)
