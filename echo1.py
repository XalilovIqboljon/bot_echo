import requests
from pprint import pprint
import os
token = "1667389228:AAHfOEBt6VXPoOqoHIgGK13p6fW-1JUTETc"
# token =os.environ['TOKEN']
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