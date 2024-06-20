#!/usr/bin/python3

""" A square class with private instance attribute: size"""

class Square:
    """Represents a square
    Attributes:
    __size (int): The size of the square
    """
    def __init__ (self, size=0):
        """initialize the class

        Args:
            size (int, optional): _description_. Defaults to 0.
        Returns:
            None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
