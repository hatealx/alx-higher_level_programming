#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = [k for k in a_dictionary]
    keys = sorted(keys)
    for key in keys:
        print(f"{key}:{a_dictionary[key]}")
