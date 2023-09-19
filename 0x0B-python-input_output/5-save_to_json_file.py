#!/usr/bin/python3
"""Write a function that writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """save object to afiles"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)       
