#! /usr/bin/env python3

landscape_list = []
with open("03/input.txt", 'r') as f:
    f1 = f.readlines()
    for item in f1:
        landscape_list.append(item.strip())

i_row = 0
i_col = 0
next_col = 0
count_trees = 0
row_len = len(landscape_list[0])

while i_row < len(landscape_list)-1:
    next_col = i_col + 3
    # print(i_row, tmp_row)
    if next_col >= row_len:
        next_col = next_col - row_len
    i_col = next_col
    i_row = i_row + 1
    tmp_row = landscape_list[i_row]
    # print(i_row, tmp_row)
    if tmp_row[next_col] == '#':
        count_trees = count_trees + 1

    #print(i_row, tmp_row[next_col])

print("nTrees:", count_trees)
