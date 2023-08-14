#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for li in matrix:
        i = 0
        for el in li:
            if (i < 2):
                print("{}".format(el), end=" ")
            else:
                print("{}".format(el), end="")
            i += 1 

        print("")
