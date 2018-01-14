# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))


def find_is_sql_files(find_string, files_list):
    result_file_list = []
    for file in files_list:
        with open(file) as f:
            reader = f.read()
            if find_string in reader:
                result_file_list.append(file)
    if len(result_file_list) > 15:
        print('...Большой список файлов...')
    else:
        for elem in result_file_list:
            print(elem)

    print('Всего {}'.format(len(result_file_list)))
    return result_file_list


if __name__ == '__main__':
    dir_migrations = os.path.join(current_dir, migrations)
    files_list = (os.path.join(migrations, sql_file_name) for sql_file_name in os.listdir(dir_migrations)
                  if sql_file_name[-3:] == 'sql')

    while True:
        find_string = input('Введите строку: ')
        files_list = find_is_sql_files(find_string, files_list)


