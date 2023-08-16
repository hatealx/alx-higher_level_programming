#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for li in matrix:
        nli = list(map(lambda el: el * el, li))
        new_matrix.append(nli)
    return new_matrix
