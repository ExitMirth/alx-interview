#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    # Iterate through the data set
    for i in data:
        if i >> 7 == 0b0:
            continue
        elif i >> 5 == 0b110:
            n = 1
        elif i >> 4 == 0b1110:
            n = 2
        elif i >> 3 == 0b11110:
            n = 3
        else:
            return False
        for _ in range(n):
            if (i >> 6) & 0b10 != 0b10:
                return False
            i = next(data, None)
            if i is None or (i >> 6) & 0b10 != 0b10:
                return False
    return True
