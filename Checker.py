import requests
import hashlib

def request_api_result(password):
    url = 'https://api.pwnedpasswords.com/range' + 'pass'
    res = requests.get(url)
    print(res)

def pwned_api_check(password):
    pass

