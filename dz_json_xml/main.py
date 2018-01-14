import json
import chardet
import xml.etree.ElementTree as ET


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


def print_top_words_from_json(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        encoding_type = chardet.detect(data)['encoding']

    with open(filename, encoding=encoding_type) as f:
        print('\nРаботаем с файлом {} (кодировка {}):'.format(filename, encoding_type))
        data = json.load(f)
        all_text = ''
        for item in data['rss']['channel']['items']:
            all_text += item['description']
            all_text += item['title']
        top_words_dict = get_top_words(all_text)
        for word in top_words_dict:
            print('-- Слово "{}" встречается {} раз'.format(word, top_words_dict[word]))


def print_top_words_from_xml(filename):
    encoding_type = ''
    with open(filename, 'rb') as f:
        data = f.read()
        encoding_type = chardet.detect(data)['encoding']
        print(encoding_type)

    print('\nРаботаем с файлом {}:'.format(filename))
    tree = ET.parse(filename)
    descriptions = tree.findall('channel/item/description')
    all_text = ''
    for description in descriptions:
        text = description.text.encode(encoding_type)
        text = text.decode(encoding_type)
        text = text.replace('<br>', ' ')
        all_text += text
    top_words_dict = get_top_words(all_text)
    for word in top_words_dict:
        print('-- Слово "{}" встречается {} раз'.format(word, top_words_dict[word]))


# print_top_words_from_file('data/newsafr.json')
# print_top_words_from_file('data/newscy.json')
# print_top_words_from_file('data/newsfr.json')
# print_top_words_from_file('data/newsit.json')

print_top_words_from_xml('data/newsit.xml')
print_top_words_from_xml('data/newsfr.xml')
# print_top_words_from_xml('data/newsit.xml')


# text = '<br><br>anananananananana <br>hfhfhfh fjfjfj<br>'
# text = text.replace('<br>', ' ')
# print(text)

# tree = ET.parse('data/newscy.xml')
# tree = ET.parse('data/newsfr.xml')
# tree = ET.parse('data/newsit.xml')
