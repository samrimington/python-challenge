"""http://www.pythonchallenge.com/pc/return/good.html"""

import os
import re

from PIL import Image, ImageDraw

def challenge_09() -> None:
    script_dir = os.path.dirname(__file__)
    first_path = os.path.join(script_dir, "first.txt")
    with open(first_path) as f:
        FIRST = [int(x) for x in re.findall(r'[0-9]+', f.read())]
    second_path = os.path.join(script_dir, "second.txt")
    with open(second_path) as f:
        SECOND = [int(x) for x in re.findall(r'[0-9]+', f.read())]
    im = Image.new('RGB', (480, 480))
    im1 = ImageDraw.Draw(im)
    im1.line(FIRST + SECOND)
    im.show()

challenge_09()
