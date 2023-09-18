#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""


class BaseGeometry:
    """A class with public attribute area"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """valide the argument value"""
        if type(value) != 'int':
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{value} must be greater than 0)
