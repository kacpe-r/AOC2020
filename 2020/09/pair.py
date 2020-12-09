from itertools import permutations

def get_data(file_path):
    with open(file_path) as f:
        return list(int(x) for x in f.read().split())

def is_number_in_sum(el, full_list, index):
    items_to_check = full_list[index - preamble:index]
    return el in [sum(i) for i in permutations(items_to_check, 2)]

def loop_over_list():
    for index, el in enumerate(full_list):
        if index >= preamble and is_number_in_sum(el, full_list, index) == False:
            return el

if __name__ == '__main__':
    preamble = 25

    full_list = get_data('./data')
    print(loop_over_list())
