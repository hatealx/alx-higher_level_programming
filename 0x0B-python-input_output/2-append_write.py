#!/usr/bin/python3
"""file does not created?"""


def append_write(filename="", text=""):
    """appending to the end"""
    with open(filename, "a+", encoding="utf8") as file:
        file.write(text)
        return len(text)
