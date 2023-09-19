#!/usr/bin/python3
"""learning  to write to a file"""


def write_file(filename="", text=""):
    """write to a file"""
    with open(filename, "a", encoding="utf8") as file:
        file.write(text)
        return len(text)
