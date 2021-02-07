import requests
from pprint import pprint
import os

token =os.environ['token_echo']
url = f'https://api.telegram.org/bot{token}/getUpdates'
r=requests.get(url)

data=r.json()
updates=data['result']
# print(r.url)
for update in updates:
    # print(update.keys())
    message = update['message']
    user = message['from']
    user_id = user['id']
    first = user.get('first_name','')
    last = user.get('last_name','')
    print(first,last,sep=' ')
# pprint(updates)