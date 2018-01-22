import os
import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(file_in, file_out, from_lang, to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param to_lang:
    :return:
    """

    if os.path.exists(file_in):
        with open(file_in, encoding='utf-8') as f:
            data = f.read()

        params = {
            'key': API_KEY,
            'text': data,
            'lang': '{}-{}'.format(from_lang, to_lang),
        }

        response = requests.get(URL, params=params)
        json_ = response.json()
        translated_data = ''.join(json_['text'])
    else:
        raise FileExistsError

    with open(file_out, 'w') as f:
        f.write(translated_data)

    return 1


cur_dir = os.path.abspath(os.path.dirname(__file__))

translate_it(os.path.join(cur_dir, 'data/ES.txt'), os.path.join(cur_dir, 'ES-RU.txt'), 'es')
translate_it(os.path.join(cur_dir, 'data/DE.txt'), os.path.join(cur_dir, 'DE-RU.txt'), 'de')
translate_it(os.path.join(cur_dir, 'data/FR.txt'), os.path.join(cur_dir, 'FR-RU.txt'), 'fr')
