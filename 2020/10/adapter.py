import itertools

def get_data(file_path):
    with open(file_path) as f:
        return list(int(x) for x in f.read().split())

def get_adapters(full_list):
    used_one = []
    used_three = []
    full_list.append(0)
    full_list = sorted(full_list)
    for index, current_adapter in enumerate(full_list):
        try:
            next_adapter = full_list[index + 1]
            if next_adapter - current_adapter == 1:
                used_one.append(current_adapter)
        except IndexError:
            pass

    for index, current_adapter in enumerate(full_list):
        try:
            next_adapter = current_adapter + 3
            if next_adapter in full_list and next_adapter not in used_one:
                used_three.append(next_adapter)
            if current_adapter in full_list and current_adapter not in used_one:
                used_three.append(current_adapter)
        except IndexError:
            pass

    used_three = sorted(list(set(used_three)))
    return len(used_one) * len(used_three)

if __name__ == '__main__':
    full_list = sorted(get_data('./data'))
    print(get_adapters(full_list))
