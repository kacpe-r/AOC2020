def count_product(file_path):
    current_year = 2020

    with open(file_path) as f:
        numbers = [int(i) for i in f.readlines()]
        for single_number in numbers:
            looked_number = current_year - single_number
            if looked_number in numbers:
               return single_number * looked_number

if __name__ == '__main__':
    print(count_product('./data'))
