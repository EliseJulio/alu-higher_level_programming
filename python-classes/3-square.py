#!/usr/bin/python3
"""
This module defines the Square class.
"""


class Square:
    """
    Represents a square.

    Attributes:
        size (int): The size of the square's sides.
    """
    def __init__(self, size=0):
        """
        Initializes the square with an optional size.

        Args:
            size (int): The size of the square's sides. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
