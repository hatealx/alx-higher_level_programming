#!/usr/bin/python
def print_matrix_integer(matrix=[[]]):
    for li in matrix:
        for el in li:
            print("{}".format(el), end=" ")
        print("")
