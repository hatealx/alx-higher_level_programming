#!/usr/bin/python3
from sys import argv


def args():
    ars = len(argv) - 1
    if (ars == 0):
        print(f"{0} arguments.")
    elif (ars == 1):
        print(f"{ars} argument:")
        print(f"{ars}: {argv[1]}")
    elif (ars > 1):
        print(f"{ars} arguments:")
        i = 1
        for el in argv:
            if (i > ars):
                break
            print(f"{i}: {argv[i]}")
            i += 1


if __name__ == "__main__":
    args()
