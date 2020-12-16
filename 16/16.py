#! /usr/bin/env python3
def read_data(in_file):
    with open(in_file, 'r') as f:
        f1 = f.read()
        elenco = f1.split("\n")
        return elenco


def get_your_ticket(data):
    i = data.index('your ticket:')
    yt = data[i+1].strip()
    yt_list = yt.split(',')
    int_yt_list = [int(k) for k in yt_list]
    return int_yt_list


def get_nearby_tickets(data):
    i = data.index('nearby tickets:')
    nt_list = []
    for j in range(i+1, len(data)):
        if len(data[j].strip()) > 0:
            nt = data[j].strip().split(',')
            nt_list.append([int(k) for k in nt])
    return nt_list


def get_range_list(range_string):
    range1 = range_string.strip()
    idx = range1.index('-')
    min_val = int(range1[0:idx])
    max_val = int(range1[idx+1:])
    list_r1 = list(range(min_val, max_val+1))
    return list_r1


def get_rules(data):
    i_end = data.index('your ticket:')
    rules_dict = {}
    all_values = []
    for j in range(0, i_end):
        if len(data[j].strip()) > 0:
            item_key, item_value = data[j].strip().split(':')
            rules_dict[item_key] = []
            range1, range2 = item_value.strip().split('or')
            list_r1 = get_range_list(range1)
            rules_dict[item_key] += list_r1
            list_r2 = get_range_list(range2)
            rules_dict[item_key] += list_r2
            all_values += list_r1
            all_values += list_r2
    all_values_set = set(all_values)
    return rules_dict, all_values_set


def parse_data(in_file):
    data_list = read_data(in_file)
    your_ticket = get_your_ticket(data_list)
    nearby_tickets = get_nearby_tickets(data_list)
    rules, all_vals = get_rules(data_list)
    return rules, all_vals, your_ticket, nearby_tickets,


def check_invalid_tickets_values(tickets, all_vals):
    invalid = []
    for item in tickets:
        common_elements = all_vals.intersection(set(item))
        if len(common_elements) < len(item):
            diff_elements = set(item).difference(set(common_elements))
            invalid += diff_elements

    final_val = sum(invalid)
    return invalid, final_val


in_file = '16/input.txt'
rules, all_vals, your_ticket, nearby_tickets = parse_data(in_file)
invalid, final_val = check_invalid_tickets_values(nearby_tickets, all_vals)
print(invalid, final_val)
