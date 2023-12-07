#!/usr/bin/python3
a = 97
while (a <= 122):
    c = chr(a)
    if ((c == 'q') or (c == 'e')):
        a += 1
        continue
    print("{}".format(c), end="")
    a += 1
