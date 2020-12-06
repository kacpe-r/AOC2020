def get_data(file_path):
    with open(file_path) as f:
        return f.read()

def get_floor_number(data):
        return data.count('(') - data.count(')')

def get_basement_position(data):
    position = 0
    for index, move in enumerate(data, start=1):
        position += 1 if move == ('(') else - 1
        while position < 0:
            return index

if __name__ == '__main__':
    print(get_floor_number(get_data('./data')))
    print(get_basement_position(get_data('./data')))
