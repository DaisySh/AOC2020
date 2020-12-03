#! /usr/bin/env python3

def check_trees(landscape_list, r_right, d_down):
    i_row = 0
    i_col = 0
    next_col = 0
    count_trees = 0
    row_len = len(landscape_list[0])
    while i_row < len(landscape_list)-1:
        next_col = i_col + r_right
        if next_col >= row_len:
            next_col = next_col - row_len
        i_col = next_col
        i_row = i_row + d_down
        if i_row > len(landscape_list):
            return count_trees
        tmp_row = landscape_list[i_row]
        if tmp_row[next_col] == '#':
            count_trees = count_trees + 1
    return count_trees


landscape_list = []
with open("03/input.txt", 'r') as f:
    f1 = f.readlines()
    for item in f1:
        landscape_list.append(item.strip())

move_list = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
multipy_trees = 1
for i_right, j_down in move_list:
    count_trees = check_trees(landscape_list, i_right, j_down)
    s = "Right {}, Down {}. nTrees {}".format(i_right, j_down, count_trees)
    multipy_trees *= count_trees
    print(s)

print('Multiply trees: ', multipy_trees)
