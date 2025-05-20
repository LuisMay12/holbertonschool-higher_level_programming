#!/usr/bin/python3
"""Module that defines a Square class with size validation and area method.

This module provides a way to create square objects, validate their size,
and compute their area using a public method.
"""


class Square:
    """Represents a square with a validated size and an area calculator.

    Attributes:
        __size (int): The size of the square, must be an integer >= 0.
    """

    def __init__(self, size=0):
        """Initializes a Square instance with optional size.

        Args:
            size (int): The size of the square (default is 0).

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
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2
