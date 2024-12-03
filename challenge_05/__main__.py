"""http://www.pythonchallenge.com/pc/def/peak.html"""

import pickle
import os

def challenge_05() -> str:
    script_dir = os.path.dirname(__file__)
    input_path = os.path.join(script_dir, "banner.pickle")
    with open(input_path, 'rb') as f:
        BANNER = pickle.load(f)
    out = ''
    for line in BANNER:
        for x, count in line:
            out += x * count
        out += '\n'
    return out

print(challenge_05())
