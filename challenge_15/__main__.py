"""http://huge:file@www.pythonchallenge.com/pc/return/uzi.html"""

from datetime import datetime

def challenge_15() -> int:
    out = []
    for year in range(1996, 1006, -10):
        # On a Monday and on a leap year
        if datetime(year, 1, 26).weekday() == 0 and\
            (year % 4 == 0 and year % 100 != 0 or (year % 100 == 0 and year % 400 == 0)):
            out.append(year)
    return out[1]  # Second youngest

print(challenge_15())
