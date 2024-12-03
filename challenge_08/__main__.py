"""http://www.pythonchallenge.com/pc/def/integrity.html"""

from typing import Tuple
import bz2

def challenge_08() -> Tuple[str, str]:
    UN = bz2.decompress(
        b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    ).decode('utf-8')
    PW = bz2.decompress(
        b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
    ).decode('utf-8')
    return UN, PW

print(challenge_08())
