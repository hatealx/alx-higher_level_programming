#!/usr/bin/python3
n = 1
for i in range(0, 8):
    for j in range(n, 10):
        if (i > j):
            j += 1
            continue
        print("{}{}, ".format(i,j), end="")
    n += 1
print("{}{}".format(8, 9))
