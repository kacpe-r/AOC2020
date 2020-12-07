from re import findall, split

def get_data(file_path):
    all_data = []
    with open(file_path) as f:
        raw_data = f.read().splitlines()
        for single_row in raw_data:
            row_groped = single_row.split(' bags contain ')
            row_object = {
                'parent': row_groped[0],
                'children': [
                    {
                        'amount': int(bag_amount),
                        'type': bag_type
                    } for bag_amount, bag_type in findall(r'(\d+) (\w*\s*\S*) bags?[,\.]', row_groped[1])
                ]
            }
            all_data.append(row_object)
    return all_data

def counter(color):
    for single_data in all_data:
        if single_data['parent'] == color:
            next_to_check = []
            for child in single_data['children']:
                for i in range(0, child['amount']):
                    next_to_check.append(child['type'])
            return [len(next_to_check), next_to_check]

if __name__ == '__main__':
    total_bags = 0
    to_check_in_future = []
    all_data = get_data('./data')

    if len(to_check_in_future) == 0:
        total_bags, to_check_in_future = counter('shiny gold')

    for color in to_check_in_future:
        number_of_bags, next_to_check = counter(color)
        total_bags += number_of_bags
        to_check_in_future += next_to_check

    print('total bags:', total_bags)
