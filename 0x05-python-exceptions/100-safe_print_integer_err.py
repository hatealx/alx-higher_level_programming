#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{}".format(value))
        return True
    except TypeError:
        raise TypeError("Exception: Unknown format code 'd' for object of type 'str'")
        return False

