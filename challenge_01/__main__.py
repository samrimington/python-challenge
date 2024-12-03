"""http://www.pythonchallenge.com/pc/def/map.html"""

def challenge_01() -> str:
    MESSAGE = '''g fmnc wms bgblr rpylqjyrc gr zw fylb.
rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
    decoded = [
        chr((ord(x) - 94) % 26 + 96) if x >= 'a' and x <= 'z' else x
        for x in MESSAGE
    ]
    return ''.join(decoded)

print(challenge_01())
