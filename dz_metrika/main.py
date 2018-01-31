from pprint import pprint
from urllib.parse import urlencode
import requests

'''site url is: https://dzendjo.github.io/test_site/'''


# APP_ID = '29c0340d901b44d9bc68749821c134c7'
# AUTH_URL = 'https://oauth.yandex.ru/authorize'
#
# params = {
#     'response_type': 'token',
#     'client_id': APP_ID
# }
#
# print('?'.join((AUTH_URL, urlencode(params))))

TOKEN = 'AQAAAAAQ5j4tAATJR89LH_MNPkZYqNx0QcRXnvo'
COUNTER_ID = 47518975


class YandexUser:

    API_URL = 'https://api-metrika.yandex.ru/stat/v1/data'

    def __init__(self, token, counter_id):
        self.token = token
        self.counter_id = counter_id
        self.headers = {
            'Authorization': 'OAuth {}'.format(self.token),
            'Content-Type': 'application/json'
        }

    @property
    def visits(self):
        params = {
            'metrics': 'ym:s:visits',
            'id': self.counter_id
        }
        response = requests.get(self.API_URL, params, headers=self.headers)
        return response.json()

    @property
    def pageviews(self):
        params = {
            'metrics': 'ym:s:pageviews',
            'id': self.counter_id
        }
        response = requests.get(self.API_URL, params, headers=self.headers)
        return response.json()

    @property
    def users(self):
        params = {
            'metrics': 'ym:s:users',
            'id': self.counter_id
        }
        response = requests.get(self.API_URL, params, headers=self.headers)
        return response.json()


user = YandexUser(TOKEN, COUNTER_ID)
pprint(user.visits)
pprint(user.pageviews)
pprint(user.users)
