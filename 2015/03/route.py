def get_data(file_path):
    with open(file_path) as f:
        return f.read()

def get_route(data):
    positions = [{'x': 0, 'y': 0}]
    unique_houses = 1
    for symbol in data:
        if symbol == '>':
            move = {'x' :positions[-1]['x'] + 1, 'y': positions[-1]['y']}
        if symbol == '<':
            move = {'x': positions[-1]['x'] - 1, 'y': positions[-1]['y']}
        if symbol == '^':
            move = {'x': positions[-1]['x'], 'y': positions[-1]['y'] + 1}
        if symbol == 'v':
            move = {'x': positions[-1]['x'], 'y': positions[-1]['y'] - 1}

        if move not in positions:
            unique_houses += 1
        positions.append(move)

    return unique_houses

if __name__ == '__main__':
    print(get_route(get_data('./data')))
