def get_number_of_valid_documents(file_path):
    mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    number_of_valid_documents = 0
    with open(file_path) as f:
        persons = f.read().split('\n\n')
        for person in persons:
            person_formatted = person.replace('\n', ' ').split(' ')
            person_dict = dict(kv.split(':') for kv in person_formatted)
            is_document_valid = all(elem in person_dict.keys() for elem in mandatory_fields)
            if is_document_valid:
                number_of_valid_documents += 1
    return number_of_valid_documents

if __name__ == '__main__':
    print(get_number_of_valid_documents('./data'))
