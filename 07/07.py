#! /usr/bin/env python3
import ast


def read_rules(in_file):
    with open(in_file, 'r') as f:
        f1 = f.read()
        elenco = f1.split("\n")
        return elenco


def rule_interpreter(r_str):
    r_clean = r_str.strip()
    res = {}
    # main bag analysis
    main_color_bag, idx_contain = def_main_color_bag(r_clean)
    res[main_color_bag] = []

    # other bags analysis
    cl = len('contain')
    r_rest = r_clean[idx_contain+cl:].strip()
    r_split = r_rest.split(',')
    if r_rest.find(',') > -1:
        for r_item in r_split:
            r_item = r_item.strip()
            res[main_color_bag].append(base_rule(r_item))
    else:
        # 1 or no additional bags included
        if r_rest.find('no other bags') == -1:
            # add color bag
            res[main_color_bag].append(base_rule(r_rest))
    return main_color_bag, res[main_color_bag]


def def_main_color_bag(main_str):
    idx_contain = main_str.find('contain')
    main_bag = main_str[:idx_contain].split(' ')
    main_color_bag = "{}-{}".format(main_bag[0], main_bag[1])
    return main_color_bag, idx_contain


def base_rule(r_str):
    r_split = r_str.split(' ')
    n_item = r_split[0]
    color_item = "{}-{}".format(r_split[1], r_split[2])
    return (n_item, color_item)


def inner_shiny(my_rules):
    my_rules_list = {}
    sg_list = set()
    sg_list.add('shiny-gold')
    sg_list_delimiter = 0
    while sg_list_delimiter != len(sg_list):
        sg_list_delimiter = len(sg_list)
        for r in my_rules:
            if len(r.strip()) > 0:
                r_color, r_items = rule_interpreter(r)
                if len(r_items) > 0:
                    for i, j in r_items:
                        if j in sg_list:
                            sg_list.add(r_color)
                if r_color not in my_rules_list:
                    my_rules_list[r_color] = r_items

    # print(my_rules_list)
    tmp = len(sg_list) - 1
    print('Color bags can contain SG', tmp)


def outer_shiny(my_rules):
    my_rules_list = {}
    for r in my_rules:
        if len(r.strip()) > 0:
            r_color, r_items = rule_interpreter(r)
            my_rules_list[r_color] = r_items
    sg_list = set()
    sg_list.add('shiny-gold')
    count_bags = "shiny-gold"
    while len(sg_list) > 0:
        # print(count_bags)
        color_item = sg_list.pop()
        check_bag = my_rules_list[color_item]
        if len(check_bag) > 0:
            tmp_elements = ""
            for i, j in check_bag:
                if len(tmp_elements) > 0:
                    tmp_elements = "{} + {}*({})".format(tmp_elements, i, j)
                else:
                    tmp_elements = "{}*({})".format(i, j)
                sg_list.add(j)
            count_bags = count_bags.replace(color_item, "1 + " + tmp_elements)
        else:
            count_bags = count_bags.replace(color_item, '1')
    count_bags = count_bags + " - 1"
    print('SG can contain', ast.literal_eval(count_bags))


in_file = '07/input.txt'
my_rules = read_rules(in_file)

# D7.1 problem
inner_shiny(my_rules)

# D7.2 problem
outer_shiny(my_rules)
