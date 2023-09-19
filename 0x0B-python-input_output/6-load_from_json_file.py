#!/usr/bin/python3
"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """ a function that creates an Object from a “JSON file"""
    with open(filename, "r", encoding="utf-8") as file:
        c = file.read()
        return json.loads(c)
