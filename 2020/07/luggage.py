from re import findall, split

def get_data(file_path):
    all_data = []
    with open(file_path) as f:
        raw_data = f.read().splitlines()
        for single_row in raw_data:
            row_groped = single_row.split(' bags contain ')
            full_row = [row_groped[0], findall(r'\d+ (\w*\s*\S*) bags?[,\.]', row_groped[1])]
            all_data.append(full_row)

    return all_data

def get_all_colors(data):
    all_colors = []
    for row in data:
        if row[0] not in all_colors:
            all_colors.append(row[0])
        for color in row[1]:
            if color not in all_colors:
                all_colors.append(color)
    return all_colors

def sort_for_sure_groups(data):
    for row_data in data:
        if row_data[1] == []:
            for_sure_not.append(row_data[0])
        else:
            for child_color in row_data[1]:
                if child_color == 'shiny gold':
                    for_sure_yes.append(row_data[0])

def update():
    new_colors_to_check = []
    for element in all_available_colors:
        if element not in for_sure_not + for_sure_yes:
            new_colors_to_check.append(element)
    return new_colors_to_check

def second_run():
    for fsy in for_sure_yes:
        for single_row in data:
            if fsy in single_row[1] and single_row[0] not in for_sure_yes not in for_sure_not:
                for_sure_yes.append(single_row[0])

if __name__ == '__main__':
    for_sure_yes = []
    for_sure_not = []
    data = get_data('./data')
    all_available_colors = get_all_colors(data)
    sort_for_sure_groups(data)
    second_run()
    print(len(for_sure_yes))