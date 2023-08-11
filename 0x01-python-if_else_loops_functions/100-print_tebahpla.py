#!/usr/bin/python3
z = 122
a = 97
s = 2
while (z >= a):
    t = s % 2
    if (t == 0):
        c = chr(z)
    else:
        c = chr(z - 32)
    print("{}".format(c), end="")
    z -= 1
    s += 1
