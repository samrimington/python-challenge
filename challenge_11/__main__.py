"""http://huge:file@www.pythonchallenge.com/pc/return/5808.html"""

import os

from PIL import Image

def challenge_11() -> None:
    script_dir = os.path.dirname(__file__)
    input_path = os.path.join(script_dir, "cave.jpg")
    im = Image.open(input_path)
    data = list(im.getdata())[::2]
    im1 = Image.new('RGB', (im.size[0], im.size[1] // 2))
    im1.putdata(data)
    im1.show()

challenge_11()
