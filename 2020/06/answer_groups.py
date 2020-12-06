def get_answer_groups(file_path):
    with open(file_path) as f:
        return f.read().split('\n\n')

def count_unique_group_answers(groups):
    return sum([len(''.join(set(group.replace('\n', '')))) for group in groups])

def count_everyones_answer(groups):
    all_matching_group = 0
    for group in groups:
        unique_letters = ''.join(set(group.replace('\n', '')))
        letters_in_group = group.replace('\n', '')
        people_in_group =  len(group.replace('\n', ' ').split(' '))
        all_matching_group += len([unique_letter for unique_letter in unique_letters if letters_in_group.count(unique_letter) == people_in_group])

    return all_matching_group

if __name__ == '__main__':
    print(count_unique_group_answers(get_answer_groups('./data')))
    print(count_everyones_answer(get_answer_groups('./data')))
