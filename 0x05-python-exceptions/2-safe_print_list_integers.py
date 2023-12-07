#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for i in range(0, x):
        a = my_list[i]
        try:
            print("{:d}".format(a), end="")
            n += 1
        except (ValueError, TypeError):
            continue
    print("\n", end="")
    return (n)
