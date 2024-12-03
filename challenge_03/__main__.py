"""http://www.pythonchallenge.com/pc/def/equality.html"""

import re
import os

def challenge_03() -> str:
    script_dir = os.path.dirname(__file__)
    input_path = os.path.join(script_dir, "mess.txt")
    with open(input_path) as f:
        MESS = f.read()
    matches = re.findall(r"[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]", MESS)
    return ''.join(matches)

print(challenge_03())
