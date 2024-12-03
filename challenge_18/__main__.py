"""http://huge:file@www.pythonchallenge.com/pc/return/balloons.html"""

import binascii
import difflib
import gzip
import os

def challenge_18() -> None:
    first = []
    second = []
    script_dir = os.path.dirname(__file__)
    input_path = os.path.join(script_dir, "deltas.gz")
    with gzip.open(input_path, 'r') as f:
        for line in f.readlines():
            line = line.strip().decode('ascii')
            first.append(line[:56].replace(' ', ''))
            second.append(line[56:].replace(' ', ''))
    both_file = open("challenge_18_both.png", 'wb')
    first_file = open("challenge_18_first.png", 'wb')
    second_file = open("challenge_18_second.png", 'wb')
    for line in difflib.ndiff(first, second):
        binary = binascii.unhexlify(line[2:])
        if line[:2] == '  ':
            both_file.write(binary)
        if line[:2] == '+ ':
            first_file.write(binary)
        if line[:2] == '- ':
            second_file.write(binary)
    both_file.close()
    first_file.close()
    second_file.close()

challenge_18()
