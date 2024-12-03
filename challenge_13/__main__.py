"""http://huge:file@www.pythonchallenge.com/pc/return/disproportional.html"""

import xmlrpc.client

def challenge_13() -> str:
    with xmlrpc.client.ServerProxy(
            'http://www.pythonchallenge.com/pc/phonebook.php') as proxy:
        return proxy.phone('Bert')

print(challenge_13())
