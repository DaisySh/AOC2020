#! /usr/bin/env python3
def read_data(in_file):
    with open(in_file, 'r') as f:
        f1 = f.read()
        elenco = f1.split(",")
        return elenco


def clean_data(in_file):
    data_list = read_data(in_file)
    new_list = []
    for item in data_list:
        if '\n' in item:
            k = item.split('\n')
            new_list.append(int(k[0]))
        else:
            new_list.append(int(item))
    return new_list


def play_memory(start_dict, last_item, start_idx, end_game_idx):
    last_card, last_idx = last_item
    i = start_idx
    while i < end_game_idx:
        # print(last_idx, last_card, start_dict)
        i = i + 1
        if last_card in start_dict:
            if len(start_dict[last_card]) > 1:
                start_dict[last_card].sort(reverse=True)
                val_list = start_dict[last_card]
                last_card = val_list[0] - val_list[1]
                last_idx = i
                if last_card not in start_dict.keys():
                    start_dict[last_card] = [i]
                else:
                    start_dict[last_card].append(i)
            else:
                last_card = 0
                last_idx = i
                if last_card not in start_dict.keys():
                    start_dict[last_card] = [i]
                else:
                    start_dict[last_card].append(i)
        else:
            start_dict[0] = [i]
            last_card = 0
            last_idx = i
    return last_card, last_idx


in_file = "15/input.txt"
mem_list = clean_data(in_file)
print(mem_list)

mem_dict = {}
for i in range(len(mem_list)):
    mem_dict[mem_list[i]] = [i+1]

last_item = (mem_list[-1], len(mem_list))
print(mem_dict)

card, idx = play_memory(mem_dict, last_item, len(mem_list), 2020)
print(card, idx)
