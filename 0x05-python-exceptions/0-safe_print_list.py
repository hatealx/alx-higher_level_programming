#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    for i in range(0, x):
        try:
            a = my_list[i]
            print(f"{a}", end="")
            n += 1
        except IndexError:
            break
    print("\n", end="")
    return (n)
