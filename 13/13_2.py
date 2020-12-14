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


def check_fist_run2(bus_ids, bus_time, st=0):
    main_id = bus_ids[0]
    main_time = st
    for i in range(1, len(bus_ids)):
        id_fusion = main_id * bus_ids[i]
        t_fusion = [main_time*main_id, bus_time[i]*bus_ids[i]]
        main_id = id_fusion
        main_time = min(t_fusion)
    print(main_id, main_time)


# D13.2
in_file = '13/input2.txt'
bus_ids, bus_time = clean_data(in_file)
print(bus_ids, bus_time)
st = 100000000000000
check_fist_run2(bus_ids, bus_time)
