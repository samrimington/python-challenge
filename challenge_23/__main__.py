"""http://butter:fly@www.pythonchallenge.com/pc/hex/bonus.html"""

def challenge_23() -> str:
    msg = "va gur snpr bs jung?"
    s = 13
    ciphered = ''.join([
        chr((ord(x) + s - 97) % 26 + 97) if x >= 'a' and x <= 'z' else x
        for x in msg
    ])
    return ciphered

print(challenge_23())
import this
