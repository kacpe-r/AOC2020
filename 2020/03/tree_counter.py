from collections import Counter

def count_trees(file_path, move):
    trees = 0
    position = {'x': 0, 'y': 0}

    with open(file_path) as f:
        data = f.read().splitlines()
        while position['y'] < len(data):
            row_length = len(data[0])
            symbol = data[position['y']][position['x'] % row_length]
            trees += symbol == '#'

            position = dict(Counter(position) + Counter(move))
    return trees

def get_product_of_multiple_routes(file_path, list_of_routes):
    total_value = 1
    for route in list_of_routes:
        total_value *= count_trees(file_path, route)
    return total_value

if __name__ == '__main__':
    print(count_trees('./data', {'x': 3, 'y': 1}))

    routes = [
        {'x': 1,'y': 1},
        {'x': 3,'y': 1},
        {'x': 5,'y': 1},
        {'x': 7,'y': 1},
        {'x': 1,'y': 2}
    ]
    print(get_product_of_multiple_routes('./data', routes))
