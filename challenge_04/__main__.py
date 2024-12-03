"""http://www.pythonchallenge.com/pc/def/linkedlist.php"""

from typing import Tuple
import re
import urllib.request

def challenge_04() -> Tuple[int, str]:
    nothing = 8022
    for _ in range(300):
        url = f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}'
        with urllib.request.urlopen(url) as f:
            body = f.read().decode('utf-8')
        match = re.search(r'and the next nothing is ([0-9]+)', body)
        if match is None:
            break
        nothing = int(match[1])
    return nothing, body

print(challenge_04())
