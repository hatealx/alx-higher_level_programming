#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value

    for keys in a_dictionary:
        val = f" {a_dictionary[keys]}"
        a_dictionary[key] = val
    return a_dictionary
