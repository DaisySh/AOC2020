#! /usr/bin/env python3
import numpy


def read_seats(in_file):
    with open(in_file, 'r') as f:
        f1 = f.read()
        elenco = f1.split("\n")
        return elenco


def seat_interpretation(str_seat, val_range):
    if len(str_seat) == 1:
        if str_seat == 'F' or str_seat == 'L':
            final_seat = val_range[0]
            return final_seat
        if str_seat == 'B' or str_seat == 'R':
            final_seat = val_range[1] - 1
            return final_seat
    else:
        seat_simbol = str_seat[0]
        str_seat = str_seat[1:]
        min_val, max_val = val_range
        val_list = list(range(min_val, max_val))
        # print(val_list)
        half_idx = int(numpy.floor(len(val_list)/2))
        if seat_simbol == 'F' or seat_simbol == 'L':
            # print(min_val, val_list[half_idx])
            final_seat = seat_interpretation(str_seat, [min_val, val_list[half_idx]])
        elif seat_simbol == 'B' or seat_simbol == 'R':
            # print(val_list[half_idx], max_val)
            final_seat = seat_interpretation(str_seat, [val_list[half_idx], max_val])
    return final_seat


# read seats
seats = read_seats('05/input.txt')
max_row = 0
max_col = 0
max_value = 0
ids_list = []
for item in seats:
    if len(item.strip()) > 0:
        seat_item = item.strip()
        row = seat_interpretation(seat_item[:-3], [0, 128])
        col = seat_interpretation(seat_item[-3:], [0, 8])
        k = row * 8 + col
        ids_list.append(k)
        # print(row, col, k)
        if k > max_value:
            max_value = k
            max_col = col
            max_row = row

info = 'Max ID:{} Seat({},{})'.format(max_value, max_row, max_col)
print(info)

# Find your seat
ids_list.sort()
all_seats_in_range = list(range(ids_list[0], ids_list[-1]+1))
diff_set = set(all_seats_in_range) - set(ids_list)
print('My seat:', diff_set)
