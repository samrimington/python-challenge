"""http://huge:file@www.pythonchallenge.com/pc/return/evil.html"""

import os

def challenge_12() -> None:
    script_dir = os.path.dirname(__file__)
    input_path = os.path.join(script_dir, "evil2.gfx")
    with open(input_path, 'rb') as f:
        data = f.read()
    for i in range(5):
        with open(f"challenge_12_{i}.jpg", 'wb') as f:
            f.write(data[i::5])

challenge_12()
