import chardet


def get_top_words(text, len_of_word = 6):
    words_list = [word for word in text.split(' ') if len(word) >= len_of_word]
    res_dict = dict()
    for word in words_list:
        if word in res_dict.keys():
            res_dict[word] += 1
        else:
            res_dict[word] = 1
    top_word_list = sorted(res_dict, key=res_dict.get)[:-11:-1]
    top_words_dict = dict()
    for word in top_word_list:
        top_words_dict[word] = res_dict[word]
    return top_words_dict


def print_top_words_from_file(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        enc_type = chardet.detect(data)
        print('Работаем с фалом: {}, его параметры кодировки:\n{}'.format(filename, enc_type))
        text = data.decode(enc_type['encoding'])
        top_words_dict = get_top_words(text)
        for word in top_words_dict:
            print('Слово "{}" встречается {} раз'.format(word, top_words_dict[word]))


print_top_words_from_file('data/newsafr.txt')
print_top_words_from_file('data/newscy.txt')
print_top_words_from_file('data/newsfr.txt')
print_top_words_from_file('data/newsit.txt')
