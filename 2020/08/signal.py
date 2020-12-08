from copy import deepcopy

def get_data(file_path):
    with open(file_path) as f:
        data = f.read().splitlines()
        return [(lambda x: [x[0], int(x[1])])(single_row.split(' ')) for single_row in data]


def get_accumulator_value(data, data_index, visited_indexes, acc_sum):
    message_type, move = data[data_index]
    if data_index not in visited_indexes:
        visited_indexes.append(data_index)
    else:
        raise Exception(acc_sum)

    if message_type == 'acc':
        acc_sum += move
        try:
            get_accumulator_value(data, data_index + 1, visited_indexes, acc_sum)
        except IndexError:
            print(acc_sum)
    elif message_type == 'jmp':
        get_accumulator_value(data, data_index + move, visited_indexes, acc_sum)
    elif message_type == 'nop':
        get_accumulator_value(data, data_index + 1, visited_indexes, acc_sum)

def get_changable_elements():
    changable_elements_indexes = []
    for index, pair in enumerate(data):
        if (pair[0] == 'jmp'):
            changable_elements_indexes.append(index)
    return changable_elements_indexes

def jmp_to_nop(data):
    indexes_of_changable_elements = get_changable_elements()
    for found_index in indexes_of_changable_elements:
        new_data = deepcopy(data)
        new_data[found_index][0] = 'nop'

        try:
            get_accumulator_value(new_data, 0, [], 0)
        except IndexError:
            break
        except Exception:
            pass

if __name__ == '__main__':
    data = get_data('./data')
    print(get_accumulator_value(data, 0, [], 0))
    print(jmp_to_nop(data))
