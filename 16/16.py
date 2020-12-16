#! /usr/bin/env python3
import numpy as np


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
            rules_dict[item_key].append(list_r1)
            list_r2 = get_range_list(range2)
            rules_dict[item_key].append(list_r2)
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
    new_tickets = []
    invalid = []
    i = 0
    for item in tickets:
        common_elements = all_vals.intersection(set(item))
        if len(common_elements) < len(set(item)):
            diff_elements = set(item).difference(set(common_elements))
            invalid += diff_elements
        elif len(common_elements) == len(set(item)):
            new_tickets.append(item)
        i += 1

    final_val = sum(invalid)
    return invalid, final_val, new_tickets


def check_rules(col_vals, rules):
    decision = False
    count = 0
    for j in col_vals:
        if j in rules[0] or j in rules[1]:
            count += 1
    if count == len(col_vals):
        decision = True
    return decision


def remove_item(my_dict, value):
    for k in my_dict.keys():
        if len(my_dict[k]) > 1 and value in my_dict[k]:
            my_dict[k].remove(value)
    return my_dict


def next_key(all_keys, combo_rule_index):
    for k in combo_rule_index.keys():
        if len(combo_rule_index[k]) == 1 and combo_rule_index[k][0] in all_keys:
            return combo_rule_index[k][0]


def clean_combo(combo_rule_index, all_keys):
    first_item = next_key(all_keys, combo_rule_index)
    while len(all_keys) > 0:
        remove_item(combo_rule_index, first_item)
        all_keys.remove(first_item)
        first_item = next_key(all_keys, combo_rule_index)
    return combo_rule_index


def analysis(tickets, rules):
    tickets_matrix = np.asarray(tickets)
    max_rows, max_cols = tickets_matrix.shape
    rules_list = rules.keys()
    combo_rule_index = {}
    for j in range(0, max_cols):
        col_vals = tickets_matrix[:, j]
        #print(col_vals)
        combo_rule_index[j] = []
        for item in rules_list:
            local_list = rules[item]
            if check_rules(col_vals, local_list):
                combo_rule_index[j].append(item)
    rl = [k for k in rules_list]
    print(clean_combo(combo_rule_index, rl))
    return combo_rule_index


in_file = '16/input.txt'
rules, all_vals, your_ticket, nearby_tickets = parse_data(in_file)
invalid, final_val, new_tickets = check_invalid_tickets_values(nearby_tickets, all_vals)
print(invalid, final_val)

# D16.2
new_tickets.append(your_ticket)
combo_rule_index = analysis(new_tickets, rules)
final_val = 1
for k, v in combo_rule_index.items():
    if v[0].find('departure') >= 0:
        final_val *= your_ticket[k]
print(final_val)
