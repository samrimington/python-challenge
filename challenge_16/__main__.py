"""http://huge:file@www.pythonchallenge.com/pc/return/mozart.html"""

import os

import numpy as np
from PIL import Image

def challenge_16() -> None:
    script_dir = os.path.dirname(__file__)
    input_path = os.path.join(script_dir, "mozart.gif")
    im = Image.open(input_path)
    data = np.array(list(im.getdata())).reshape((im.size[1], im.size[0]))
    newData = np.zeros((data.shape[0], data.shape[1] * 2))
    rows, indexes = np.where(data == 195)
    for x, y in zip(rows, indexes):
        if any(newData[x]):
            continue
        offset = im.size[0] - y
        newData[x, offset:offset + im.size[0]] = data[x]
    im1 = im.resize((newData.shape[1], newData.shape[0]))
    im1.putdata(newData.flatten())
    im1.show()

challenge_16()
