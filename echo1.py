import requests
from pprint import pprint
import os
token = '1623452611:AAHhPixDjQH2sre-onqGwwrBaamPZ5Uvips'
url = f'https://api.telegram.org/bot{token}/getMe'
r=requests.get(url)

pprint(r.json())