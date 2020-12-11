#! /usr/bin/env python3
import numpy as np


def read_data(in_file):
    with open(in_file, 'r') as f:
        f1 = f.read()
        elenco = f1.split("\n")
        return elenco


def clean_data(in_file):
    data_list = read_data(in_file)
    for i in range(len(data_list)):
        if len(data_list[i].strip()) > 0:
            data_list[i] = list(data_list[i].strip())
        else:
            break
    data_list = data_list[:i]
    data = np.asarray(data_list)
    return data


def check_seat(data, i, j):
    set_i = [i-1, i, i+1]
    set_j = [j-1, j, j+1]
    max_row, max_col = data.shape
    all_seats = []
    for ki in set_i:
        if ki >= 0 and ki < max_row:
            for kj in set_j:
                if kj >= 0 and kj < max_col:
                    all_seats.append(data[ki][kj])
    all_seats.remove(data[i][j])
    return all_seats


def take_seat(data):
    tmp_data = data.copy()
    seat_flag = False
    max_row, max_col = data.shape
    for i in range(max_row):
        for j in range(max_col):
            item = data[i][j]
            local_seats = check_seat(data, i, j)
            if item == 'L':
                if '#' not in local_seats:
                    tmp_data[i][j] = '#'
                    seat_flag = True
            elif item == '#':
                occ = local_seats.count('#')
                if occ >= 4:
                    tmp_data[i][j] = 'L'
                    seat_flag = True
    return seat_flag, tmp_data


def print_ferry(data):
    max_row, max_col = data.shape
    for i in range(max_row):
        s = ""
        for j in range(max_col):
            s = "{} {}".format(s, data[i][j])
        print(s)
    print("\n")


def ferry_seats(data):
    seat_flag = True
    # print_ferry(data)
    while seat_flag:
        # print(seat_flag)
        seat_flag, data = take_seat(data)
        # print_ferry(data)

    d = data.flatten().tolist()
    return d.count('#')


in_file = "11/input.txt"
data = clean_data(in_file)

# D11.1 lentoooooo
cs = ferry_seats(data)
print('Occupied seats ', cs)
