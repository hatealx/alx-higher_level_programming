#!/usr/bin/python3
"""learning to open files"""


def read_file(filename=""):
    """read a file and prints its content"""
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
