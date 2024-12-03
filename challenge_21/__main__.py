"""challenge_21.zip"""


import bz2
import os
import zlib

def challenge_21() -> str:
    script_dir = os.path.dirname(__file__)
    input_path = os.path.join(script_dir, "package.pack")
    with open(input_path, 'rb') as f:
        content = f.read()
    for i in range(800):
        #print(i, content[:50])
        if content.startswith(b'x\x9c'):
            print('#', end='')
            content = zlib.decompress(content)
        elif content.startswith(b'BZh'):
            print(' ', end='')
            content = bz2.decompress(content)
        else:
            print()
            content = content[::-1]
    return content.decode('ascii')

print(challenge_21())
