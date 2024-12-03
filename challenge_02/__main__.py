"""http://www.pythonchallenge.com/pc/def/ocr.html"""

import re
import os

def challenge_02() -> str:
    script_dir = os.path.dirname(__file__)
    input_path = os.path.join(script_dir, "mess.txt")
    with open(input_path) as f:
        MESS = f.read()
    return re.sub(r'[^a-z]', '', MESS)

print(challenge_02())
