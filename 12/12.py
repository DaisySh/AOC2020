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


# D12.1
in_file = "12/input.txt"
data = clean_data(in_file)

dirs = {'E': 0, 'W': 0, 'N': 0, 'S': 0}
check_dirs = {'E': 'W', 'W': 'E', 'N': 'S', 'S': 'N'}
degree = [0, 90, 180, 270]
coo_degree = 'NESW'
face = 'E'
left_right = ['R', 'L']

print(dirs)
for item in data:
    symbol = item[0]
    value = int(item[1:])
    # print(item, face)
    if symbol == 'F':
        dirs[face] += value
        face_buddy = check_dirs[face]
        if dirs[face_buddy] > 0:
            face_value, face_buddy_value = check_buddy(dirs, face, face_buddy)
            dirs[face] = face_value
            dirs[face_buddy] = face_buddy_value
    elif symbol in left_right:
        face_degree = degree[coo_degree.index(face)]
        if symbol == 'R':
            face_degree += value
        else:
            face_degree = face_degree - value + 360
        tmp_degree = face_degree % 360
        face = coo_degree[degree.index(tmp_degree)]
    else:
        # symbol = NSWE
        dirs[symbol] += value
        symbol_buddy = check_dirs[symbol]
        if dirs[symbol_buddy] > 0:
            symbol_value, symbol_buddy_value = check_buddy(dirs, symbol, symbol_buddy)
            dirs[symbol] = symbol_value
            dirs[symbol_buddy] = symbol_buddy_value
    # print("-->", face, dirs)

print(dirs)
man_distance = abs(dirs['E'] - dirs['W']) + abs(dirs['N'] - dirs['S'])
print("Man distance: ", man_distance)
