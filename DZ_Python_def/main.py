documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }


def people(n_of_document):
    for i, element in enumerate(documents):
        if n_of_document in element.values():
            return element['name']
    return 'Cannot find document'


def print_list():
    for i, element in enumerate(documents):
        print('{} "{}" "{}"'.format(element['type'], element['number'], element['name']))


def print_dir():
    print(directories)


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def find_shelf(n_of_document):
    for element in directories.values():
        if n_of_document in element:
            return get_key(directories, element)
    return 'Cannot find document'


def add_person(document_number, type_document, name_owner, shelf_number):
    documents.append({'type': type_document, 'number': document_number, 'name': name_owner})
    if shelf_number in directories.keys():
        directories[shelf_number].append(document_number)
    else:
        directories[shelf_number] = []
        directories[shelf_number].append(document_number)


while True:
    com = input('\nEnter command: \np - search person by number of document\nl - list\nls - list shelves\ns - shelf\na - add\nq - exit\n')
    if com == 'p':
        document_number = input('Enter document number: ')
        print(people(document_number))
    elif com == 'l':
        print_list()
    elif com == 'ls':
        print_dir()
    elif com == 's':
        document_number = input('Enter document number: ')
        print('Document on the shelf with number - {}'.format(find_shelf(document_number)))
    elif com == 'a':
        document_number = input('Enter document number: ')
        type_document = input('Enter type of document: ')
        name_owner = input('Enter name of owner: ')
        shelf_number = input('Enter shelf number: ')
        add_person(document_number, type_document, name_owner, shelf_number)
        print('Person added')
    elif com == 'q':
        print('Exit program...')
        break
    else:
        print('Unaviable command!')
