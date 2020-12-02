from re import findall

def get_correct_passwords_number(file_path):
    matching_passords_count = 0
    with open(file_path) as f:
        for data_line in f.readlines():
            data_list = findall(r'\w+', data_line)
            min = int(data_list[0])
            max = int(data_list[1])
            amount = data_list[3].count(data_list[2])
            if min <= amount <= max: matching_passords_count += 1
    return matching_passords_count

if __name__ == '__main__':
    print(get_correct_passwords_number('./data'))
