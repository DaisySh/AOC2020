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
    data_list = data_list[:i]
    return data_list


def get_bin(x, n=0):
    """
    Get the binary representation of x.

    Parameters
    ----------
    x : int
    n : int
        Minimum number of digits. If x needs less digits in binary, the rest
        is filled with zeros.

    Returns
    -------
    str
    """
    return format(x, 'b').zfill(n)


def mask_memory(mask_bit, mem_value):
    b_mem_value = get_bin(mem_value, len(mask_bit))
    new_val = ''
    # print(b_mem_value)
    # print(mask_bit)
    for i in range(len(mask_bit)):
        if mask_bit[i] != 'X':
            new_val += mask_bit[i]
        else:
            new_val += b_mem_value[i]
    # print(new_val)
    return int(new_val, base=2)


def get_mem_index(mem_string):
    idx1 = mem_string.index('[')
    idx2 = mem_string.index(']')
    return mem_string[idx1+1:idx2]


in_file = "14/input.txt"
mem_list = clean_data(in_file)
mask_bit = ''
mem_dict = {}
for item in mem_list:
    m_tag, m_value = item.split('=')
    if m_tag.strip() == 'mask':
        mask_bit = m_value.strip()
    else:
        # print(item)
        mem_id = get_mem_index(m_tag)
        mem_value = int(m_value.strip())
        mem_update = mask_memory(mask_bit, mem_value)
        mem_dict[mem_id] = mem_update

print(mem_dict)
res_sum = 0
for k, v in mem_dict.items():
    if v > 0:
        res_sum += v

print('Non zero sum:', res_sum)
