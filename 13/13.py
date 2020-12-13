#! /usr/bin/env python3
import math


def read_data(in_file):
    with open(in_file, 'r') as f:
        f1 = f.read()
        elenco = f1.split("\n")
        return elenco


def clean_data(in_file):
    data_list = read_data(in_file)
    timestamp = int(data_list[0].strip())
    bus_list = data_list[1].strip().split(',')
    bus_ids = []
    for item in bus_list:
        if item != 'x':
            bus_ids.append(int(item))
    return timestamp, bus_ids


def check_runs(bus_list, timestamp):
    best_id = 0
    best_time = math.inf
    for item in bus_list:
        max_val = max(list(range(0, timestamp, item)))
        tmp = max_val + item
        if best_time > tmp:
            best_id = item
            best_time = tmp
    return best_id, best_time


in_file = '13/input.txt'
t, bus = clean_data(in_file)
best_id, best_time = check_runs(bus, t)
s = "ID:{} starts:{} ID*diff:{}".format(best_id, best_time, best_id*(best_time-t))
print(s)
