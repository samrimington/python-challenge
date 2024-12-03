"""http://www.pythonchallenge.com/pc/def/oxygen.html"""

import re
import os

from PIL import Image

def challenge_07() -> str:
    script_dir = os.path.dirname(__file__)
    input_path = os.path.join(script_dir, "oxygen.png")
    im = Image.open(input_path)
    data = list(im.getdata())
    startAt = im.size[0] * (im.size[1] // 2) + 1
    row = data[startAt:startAt + im.size[0]:7]
    message = ''.join(chr(x[0]) for x in row)
    matches = re.findall(r'[0-9]+', message)
    return ''.join(chr(int(x)) for x in matches)

print(challenge_07())
