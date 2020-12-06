def get_data(file_path):
    with open(file_path) as f:
        return f.read()

def get_route(data):
    positions = [{'x': 0, 'y': 0}]
    unique_houses = 1
    for symbol in data:
        move = move_to_next(positions[-1], symbol)

        if move not in positions:
            unique_houses += 1
        positions.append(move)

    return unique_houses

def move_to_next(previous_position, direction):
    if direction == '>':
        move = {'x' : previous_position['x'] + 1, 'y': previous_position['y']}
    if direction == '<':
        move = {'x': previous_position['x'] - 1, 'y': previous_position['y']}
    if direction == '^':
        move = {'x': previous_position['x'], 'y': previous_position['y'] + 1}
    if direction == 'v':
        move = {'x': previous_position['x'], 'y': previous_position['y'] - 1}
    return move

if __name__ == '__main__':
    print(get_route(get_data('./data')))
