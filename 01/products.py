from itertools import combinations
from functools import reduce

def count_product(file_path, number_of_products):
    current_year = 2020

    with open(file_path) as f:
        numbers = [int(i) for i in f.readlines()]

        set_of_three = (i for i in combinations(numbers, number_of_products) if sum(i) == current_year)
        for i in set_of_three:
            return (reduce(lambda x, y: x*y, i))

if __name__ == '__main__':
    print(count_product('./data', 2))
    print(count_product('./data', 3))
