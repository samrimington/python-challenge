"""http://huge:file@www.pythonchallenge.com/pc/return/italy.html"""

import os

import numpy as np
from PIL import Image

def challenge_14() -> None:
    def spiralClockwise(A: np.array) -> np.array:
        out = np.empty(A.shape, dtype='object')
        n = 0
        while (A.size):
            x = -n if n else None
            out[n, n:x] = A[0]  # Top
            A = A[1:].reshape(A.shape[1], A.shape[1] - 1, 3)
            out[n + 1:x, -n - 1] = A[0]  # Right
            y = n - 1 if n else None
            out[-n - 1, -n - 2:y:-1] = A[1]  # Bottom
            A = A[2:].reshape(A.shape[1], A.shape[1] - 1, 3)
            out[-n - 2:n:-1, n] = A[0]  # Left
            A = A[1:]
            n += 1
        return out

    script_dir = os.path.dirname(__file__)
    input_path = os.path.join(script_dir, "wire.png")
    im = Image.open(input_path)
    data = np.array(list(im.getdata())).reshape(100, 100, 3)
    spiraled = spiralClockwise(data)
    spiraled = spiraled.reshape(spiraled.size // 3, 3)
    im1 = Image.new('RGB', (100, 100))
    im1.putdata([tuple(x) for x in spiraled])
    im1.show()

challenge_14()
