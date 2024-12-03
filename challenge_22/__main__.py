"""http://butter:fly@www.pythonchallenge.com/pc/hex/copper.html"""

import os

from PIL import Image, ImageDraw

def challenge_22() -> None:
    script_dir = os.path.dirname(__file__)
    input_path = os.path.join(script_dir, "white.gif")
    im = Image.open(input_path)
    im2 = Image.new('RGB', im.size)
    draw = ImageDraw.Draw(im2)
    shapes = []
    for i in range(im.n_frames):
        im.seek(i)
        data = [(i % im.size[0] - 100, i // im.size[0] - 100)
                for i, x in enumerate(im.getdata()) if x not in [0, (0, 0, 0)]]
        if data:
            x, y = data[0][0], data[0][-1]
            if x == 0 and y == 0:
                start = 30 * (len(shapes) + 1)
                shapes.append([(start, start)])
            else:
                x2, y2 = shapes[-1][-1]
                shapes[-1].append((x + x2, y + y2))
    for shape in shapes:
        draw.line(shape, fill="white", width=0)
    im2.show()

challenge_22()
