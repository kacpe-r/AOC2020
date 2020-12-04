from re import search

def get_valid_documents(file_path):
    valid_users = []
    mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    with open(file_path) as f:
        persons = f.read().split('\n\n')
        for person in persons:
            person_formatted = person.replace('\n', ' ').split(' ')
            person_dict = dict(kv.split(':') for kv in person_formatted)
            is_document_valid = all(elem in person_dict.keys() for elem in mandatory_fields)
            if is_document_valid:
                valid_users.append(person_dict)
    return valid_users

def is_height_correct(height):
    if 'cm' in height:
        return 149 < int(''.join(filter(str.isdigit, height))) < 194
    else:
        return 58 < int(''.join(filter(str.isdigit, height))) < 77

def get_number_of_strong_validated_documents(prevalidated_documents):
    valid_documents = 0
    for document in prevalidated_documents:
        validators = [
            int(document['byr']) in range(1920, 2003),
            int(document['iyr']) in range(2010, 2021),
            int(document['eyr']) in range(2020, 2031),
            is_height_correct(document['hgt']),
            search(r'^#[0-9a-fA-F]{6}$', document['hcl']),
            document['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
            search(r'^\d{9}$', document['pid']),
        ]

        if all(validators): valid_documents += 1
    return valid_documents

if __name__ == '__main__':
    print(len(get_valid_documents('./data')))
    print(get_number_of_strong_validated_documents(get_valid_documents('./data')))
