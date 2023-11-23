#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_ap = tuple_a + (0, 0)
    tuple_bp = tuple_b + (0, 0)
    tuple_c = ((tuple_ap[0] + tuple_bp[0]), (tuple_ap[1] + tuple_bp[1]))
    return (tuple_c)
