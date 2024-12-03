import bz2
import re
import urllib
import xmlrpc.client

import requests

def challenge_17_1() -> str:
    
    infos = []
    busynothing = 12345
    for _ in range(300):
        url = f'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={busynothing}'
        res = requests.get(url)
        body = res.content.decode('utf-8')
        infos.append(res.cookies['info'])
        match = re.search(r'and the next busynothing is ([0-9]+)', body)
        if match is None:
            break
        busynothing = int(match[1])
    combined = ''.join(infos)
    unquoted = urllib.parse.unquote(combined, 'latin1')
    bytestr = bytes(unquoted, 'latin1')
    return bz2.decompress(bytestr).decode('utf-8')


def challenge_17_2() -> str:
    with xmlrpc.client.ServerProxy(
            'http://www.pythonchallenge.com/pc/phonebook.php') as proxy:
        return proxy.phone('Leopold')


def challenge_17_3() -> str:
    res = requests.get('http://www.pythonchallenge.com/pc/stuff/violin.php',
                       cookies={'info': 'the flowers are on their way'})
    return res.content.decode('utf-8')

"""http://huge:file@www.pythonchallenge.com/pc/return/romance.html"""
print(challenge_17_1())

print(challenge_17_2())

"""http://huge:file@www.pythonchallenge.com/pc/return/violin.html"""
print(challenge_17_3())
