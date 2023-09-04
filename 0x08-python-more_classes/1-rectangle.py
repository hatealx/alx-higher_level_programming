#!/usr/bin/python3
"""
Defines a  class Rectangle
"""


class Rectangle:
    """representation of a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter of the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of the instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """getter of the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of the instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must me be an integer")
        if value < 0:
            raise ValueError("height must be  >= 0")
