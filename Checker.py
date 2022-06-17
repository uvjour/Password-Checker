import requests
import hashlib

url = 'https://api.pwnedpasswords.com/range', 'pass'
res = requests.get(url)
print(res)