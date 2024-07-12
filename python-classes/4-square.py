#!/usr/bin/python3
"""
This module defines a class Square.
"""


class Square:
    """
    A class used to represent a square.
    
    Attributes
    ----------
    size : int
        The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes the square with a given size.

        Parameters
        ----------
        size : int
            The size of the square (default is 0).

        Raises
        ------
        TypeError
            If size is not an integer.
        ValueError
            If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns
        -------
        int
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Parameters
        ----------
        value : int
            The size to set.

        Raises
        ------
        TypeError
            If value is not an integer.
        ValueError
            If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the area of the square.

        Returns
        -------
        int
            The area of the square.
        """
        return self.__size * self.__size
