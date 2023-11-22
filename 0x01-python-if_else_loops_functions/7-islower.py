#!/usr/bin/python3
def islower(c):
    a = ord(c)
    if a in range(ord('a'), ord('z') + 1):
        return (True)
    else:
        return (False)
