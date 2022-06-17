import requests
import hashlib

def request_api_result(get_char):
    url = 'https://api.pwnedpasswords.com/range' + 'pass'
    res = requests.get(url)
    return res

def pwned_api_check(password):
    hashPassword = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    initial5 = hashPassword[:5]
    restPassword = hashPassword[5:]
    response = request_api_result(initial5)
    
    return response





