#! /usr/bin/env python3
import math


def read_data(in_file):
    with open(in_file, 'r') as f:
        f1 = f.read()
        elenco = f1.split("\n")
        return elenco


def clean_data(in_file):
    data_list = read_data(in_file)
    bus_list = data_list[1].strip().split(',')
    bus_ids = []
    bus_time = []
    for item in bus_list:
        if item != 'x':
            idx = bus_list.index(item)
            bus_ids.append(int(item))
            bus_time.append(int(idx))
    return bus_ids, bus_time


def check_fist_run(bus_ids, bus_time, st=0):
    main_id = bus_ids[0]
    main_time = st
    please_stop = False
    while not please_stop:
        tmp = main_time + main_id
        stop = True
        for i in range(1, len(bus_ids)):
            if (tmp + bus_time[i]) % bus_ids[i] != 0:
                stop = False
                break
        main_time = tmp
        please_stop = stop
    return main_time


def bus_fusion(bus_ids, bus_time):
    max_id, min_id = bus_ids
    max_time, min_time = bus_time
    i = -1
    please_stop = False
    while not please_stop:
        i = i+1
        t_val = max_id * i - max_time + min_time
        # print(i, t_val)
        if t_val % min_id == 0:
            please_stop = True
            break

    fusion_id = max_id * min_id
    fusion_time = fusion_id - (max_id*i - max_time)
    return fusion_id, fusion_time


def check_fist_combo(bus_ids, bus_time):
    a_bus = bus_ids.copy()
    a_bus.sort(reverse=True)
    a_time = [bus_time[bus_ids.index(i)] for i in a_bus]
    while len(a_bus) >= 2:
        # bus
        bi1 = a_bus[0]
        bi2 = a_bus[1]
        # time
        bt1 = a_time[0]
        bt2 = a_time[1]
        # fusion
        fi, ft = bus_fusion([bi1, bi2], [bt1, bt2])
        a_bus = [fi] + a_bus[2:]
        a_time = [ft] + a_time[2:]

    return (a_bus[0] - a_time[0])


# D13.2
in_file = '13/input.txt'
bus_ids, bus_time = clean_data(in_file)
print(bus_ids, bus_time)
bt = check_fist_combo(bus_ids, bus_time)
print('First time combo at ', bt)
