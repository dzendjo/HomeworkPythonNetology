from urllib.parse import urlencode
import requests

# APP_ID = '6346172'
# URL = 'https://oauth.vk.com/authorize'
#
# auth_params = {
#     'client_id': APP_ID,
#     'redirect_uri': 'https://oauth.vk.com/blank.html',
#     'scope': 'friends',
#     'response_type': 'token',
#     'v': '5.71',
#     'display': 'popup'
# }
# # print('?'.join((URL, urlencode(auth_params))))
#
#
# request_params = {
#     'access_token': ACCESS_TOKEN,
#     'user_id': 1,
#     'text': 'Hi, bro!'
# }
# response = requests.get('https://api.vk.com/method/friends.add', request_params)
# print(response.text)

ACCESS_TOKEN = '11366a6b2d3b6e8335ea1fd6cec75deee3198924df8dac69b9ff9801f4931a2757d357248bab218c3dab6'
API_URL_MUTUAL = 'https://api.vk.com/method/friends.getMutual'
API_URL_USERS_GET = 'https://api.vk.com/method/users.get'
URL_VK = 'https://vk.com/'


def get_mutual_vk(*args):
    params = {
        'access_token': ACCESS_TOKEN,
        'source_uid': args[0],
        'target_uids': ','.join(str(i) for i in args[1:])
    }
    response = requests.get(API_URL_MUTUAL, params).json()

    common_friends = set(response['response'][0]['common_friends'])
    for friends in response['response'][1:]:
        common_friends &= set(friends['common_friends'])

    params = {
        'user_ids': ','.join(str(i) for i in common_friends),
        'fields': 'domain'
    }
    response_user_ids = requests.get(API_URL_USERS_GET, params).json()

    result_dict = {}
    for user in response_user_ids['response']:
        result_dict[user['uid']] = URL_VK + user['domain']

    return result_dict


print('Если просто 2 пользователя: ', get_mutual_vk(45, 5))
print('\nЕсли больше 2х пользователей: ', get_mutual_vk(45, 5, 6))

