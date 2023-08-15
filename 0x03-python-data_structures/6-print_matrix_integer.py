#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for li in matrix:
        n = "\n"
        i = 0
        for el in li:
            if (i < 2):
                print("{:d}".format(el), end=" ")
            else:
                print("{:d}".format(el), end="")
            i += 1

        print("{}".format(n), end="")
