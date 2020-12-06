from re import findall
from functools import reduce

def get_data(file_path):
    with open(file_path) as f:
        return f.read().split('\n')

def get_wrapping_paper_area(data):
    required_paper_amount = 0
    for package in data:
        sotred_list = sorted([int(value) for value in findall(r'(\d+)', package)])
        required_paper_amount += sum([
            3 * sotred_list[0] * sotred_list[1],
            2 * sotred_list[0] * sotred_list[2],
            2 * sotred_list[1] * sotred_list[2]
        ])
    return required_paper_amount

def get_ribbon_length(data):
    required_ribbon_length = 0
    for package in data:
        sotred_list = sorted([int(value) for value in findall(r'(\d+)', package)])
        required_ribbon_length += sum([
            2 * sotred_list[0],
            2 * sotred_list[1],
            reduce((lambda x, y: x * y), sotred_list)
        ])
    return required_ribbon_length

if __name__ == '__main__':
    print(get_wrapping_paper_area(get_data('./data')))
    print(get_ribbon_length(get_data('./data')))
