"""http://butter:fly@www.pythonchallenge.com/pc/hex/idiot2.html"""

import re

import requests
from requests.auth import HTTPBasicAuth

def challenge_20_1() -> str:
    msg = ''
    n = 30203
    for _ in range(10):
        res = requests.get('http://www.pythonchallenge.com/pc/hex/unreal.jpg',
                           auth=HTTPBasicAuth('butter', 'fly'),
                           headers={'Range': f'bytes={n}-'})
        if not res.ok:
            break
        msg += res.text
        if not res.ok:
            break
        match = re.search(r'bytes \d+-(\d+)\/\d+',
                          res.headers['Content-Range'])
        if match is None:
            break
        n = int(match[1]) + 1
    return msg


def challenge_20_2() -> str:
    msg = ''
    n = 2123456789 + 1
    for _ in range(10):
        res = requests.get('http://www.pythonchallenge.com/pc/hex/unreal.jpg',
                           auth=HTTPBasicAuth('butter', 'fly'),
                           headers={'Range': f'bytes={n}-'})
        if not res.ok:
            break
        msg += res.text
        match = re.search(r'bytes (\d+)-\d+\/\d+',
                          res.headers['Content-Range'])
        if match is None:
            break
        n = int(match[1]) - 1
    return msg


def challenge_20_3() -> None:
    res = requests.get('http://www.pythonchallenge.com/pc/hex/unreal.jpg',
                       auth=HTTPBasicAuth('butter', 'fly'),
                       headers={'Range': f'bytes=1152983631-'})
    with open('challenge_21.zip', 'wb') as f:
        f.write(res.content)

print(challenge_20_1())
print(challenge_20_2())
challenge_20_3()
