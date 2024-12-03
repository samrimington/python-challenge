"""http://www.pythonchallenge.com/pc/def/channel.html"""

import re
import os
import zipfile

def challenge_06() -> str:
    nothing = 90052
    out = ''
    script_dir = os.path.dirname(__file__)
    input_path = os.path.join(script_dir, "channel.zip")
    with zipfile.ZipFile(input_path) as channel:
        for _ in range(2000):
            name = f'{nothing}.txt'
            out += channel.getinfo(name).comment.decode('utf-8')
            with channel.open(name) as f:
                body = f.read().decode('utf-8')
            match = re.search(r'Next nothing is ([0-9]+)', body)
            if match is None:
                break
            nothing = int(match[1])
    return out

print(challenge_06())
