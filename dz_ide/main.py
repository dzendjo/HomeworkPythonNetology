def read_files(*args):
    """
    Функция для чтения из файлов. Возвращает сырой текст.
    """
    raw_data = ''
    for file_name in args:
        with open(file_name, encoding='utf-8') as f:
            current_file_data = f.read()
            raw_data += current_file_data
    return raw_data


def count_words(words_list):
    """
    Функция для вычленения и подсчета слов. Возвращает словарь вида "слово" : количество вхождений
    """
    res_dict = dict()
    for word in words_list:
        if word in res_dict.keys():
            res_dict[word] += 1
        else:
            res_dict[word] = 1
    return res_dict


data = read_files('data/newsafr.txt')
words_list = [word for word in data.split(' ') if len(word) >= 6]
counted_words_dict = count_words(words_list)
top_word_list = sorted(counted_words_dict, key=counted_words_dict.get)[:-11:-1]

for word in top_word_list:
    print('Слово {} встречается {} раз'.format(word, counted_words_dict[word]))

