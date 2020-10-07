import base64
"""
s = 'ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sSU8AaAw='
ct = base64.b64decode(s)

pt = '{"showpassword":"no","bgcolor":"#ffffff"}'

key = ''
for i in range(0, len(pt)):
	key += chr(ord(pt[i]) ^ ord(ct[i]))
print(key)
"""
pt = '{"showpassword":"yes","bgcolor":"#ffffff"}'
key = 'qw8J'
ct = ''

for i in range(0, len(pt)):
	ct += chr(ord(pt[i]) ^ ord(key[i % len(key)]))
ct = base64.b64encode(ct)
print(ct)