#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}

    for keys in a_dictionary:
        val = a_dictionary[keys]
        val2 = val * 2
        new_dic[keys] = val2

    return new_dic
