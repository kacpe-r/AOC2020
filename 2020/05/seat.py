def get_sorted_list(file_path):
    with open(file_path) as f:
        return sorted(f.read().splitlines())

def get_highest_seat(sorted_data):
    return [seat for seat in sorted_data if seat.startswith(sorted_data[0][:7])][-1]

def get_number(seat):
    row = int(seat[:7].replace('B', '1').replace('F', '0'), 2)
    column = int(seat[7:].replace('R', '1').replace('L', '0'), 2)
    return row * 8 + column

def get_my_seat(sorted_data):
    full_list = sorted([get_number(seat) for seat in sorted_data])
    return [i for i in range(full_list[0], full_list[-1]) if i not in full_list][0]

if __name__ == '__main__':
    print(get_number(get_highest_seat(get_sorted_list('./data'))))
    print(get_my_seat(get_sorted_list('./data')))
