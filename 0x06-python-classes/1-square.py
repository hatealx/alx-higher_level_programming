#!/usr/bin/python3
"""defines class square """


class Square:
    """this class represent a square
    Attributes:
       __size (int): size of one side
    """

    def __init__(self, size):
        """Initialise a square
        Args:
             size (int): size of a side of one square
        return: None
        """
        self.__size = size
