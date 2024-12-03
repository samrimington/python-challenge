"""http://huge:file@www.pythonchallenge.com/pc/return/bull.html"""

import itertools

def challenge_10() -> int:
    a = ['1']
    for _ in range(30):
        groups = itertools.groupby(a[-1])
        strings = [
            f'{len(list(repeats))}{letter}' for letter, repeats in groups
        ]
        a.append(''.join(strings))
    return len(a[30])

print(challenge_10())
