#! /usr/bin/env python3
def read_data(in_file):
    with open(in_file, 'r') as f:
        f1 = f.read()
        elenco = f1.split("\n")
        return elenco


def clean_data(in_file):
    data_list = read_data(in_file)
    for i in range(len(data_list)):
        if len(data_list[i].strip()) == 0:
            break
        else:
            data_list[i] = data_list[i].strip()
    return data_list[:i]


def check_buddy(dirs, face, face_buddy):
    face_value = 0
    face_buddy_value = 0
    if dirs[face] > dirs[face_buddy]:
        face_value = dirs[face] - dirs[face_buddy]
    if dirs[face] < dirs[face_buddy]:
        face_buddy_value = dirs[face_buddy] - dirs[face]
    return face_value, face_buddy_value


def ship2waypoint(ship_dirs, way_dirs, value):
    for k_dir, k_val in way_dirs.items():
        if k_val > 0:
            ship_dirs[k_dir] += k_val * value
            face_buddy = check_dirs[k_dir]
            if ship_dirs[face_buddy] > 0:
                face_value, face_buddy_value = check_buddy(ship_dirs, k_dir, face_buddy)
                ship_dirs[k_dir] = face_value
                ship_dirs[face_buddy] = face_buddy_value
    return ship_dirs


def rotate_waypoint(way_dirs, symbol, value):
    degree = [0, 90, 180, 270]
    coo_degree = 'NESW'
    tmp_way_dict = {'E': 0, 'W': 0, 'N': 0, 'S': 0}
    for k_dir, k_val in way_dirs.items():
        if k_val > 0:
            face_degree = degree[coo_degree.index(k_dir)]
            if symbol == 'R':
                face_degree += value
            else:
                face_degree = face_degree - value + 360
            tmp_degree = face_degree % 360
            face = coo_degree[degree.index(tmp_degree)]
            tmp_way_dict[face] = k_val
    return tmp_way_dict


# D12.2
in_file = "12/input.txt"
data = clean_data(in_file)

dirs = {'E': 0, 'W': 0, 'N': 0, 'S': 0}
ship_dirs = {'E': 0, 'W': 0, 'N': 0, 'S': 0}
way_dirs = {'E': 10, 'W': 0, 'N': 1, 'S': 0}
check_dirs = {'E': 'W', 'W': 'E', 'N': 'S', 'S': 'N'}
left_right = ['R', 'L']

for item in data:
    symbol = item[0]
    value = int(item[1:])
    # print(item, ship_dirs, way_dirs)
    if symbol == 'F':
        ship_dirs = ship2waypoint(ship_dirs, way_dirs, value)
    elif symbol in left_right:
        way_dirs = rotate_waypoint(way_dirs, symbol, value)
    else:
        # move waypoint
        # symbol = NSWE
        way_dirs[symbol] += value
        symbol_buddy = check_dirs[symbol]
        if way_dirs[symbol_buddy] > 0:
            symbol_value, symbol_buddy_value = check_buddy(way_dirs, symbol, symbol_buddy)
            way_dirs[symbol] = symbol_value
            way_dirs[symbol_buddy] = symbol_buddy_value
    # print(item, ship_dirs, way_dirs)

print(ship_dirs)
man_distance = abs(ship_dirs['E'] - ship_dirs['W']) + abs(ship_dirs['N'] - ship_dirs['S'])
print("Man distance: ", man_distance)
