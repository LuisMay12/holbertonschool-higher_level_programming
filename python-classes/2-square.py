#!/usr/bin/python3
"""Module that defines a Square class with size validation.

This module extends the Square class by validating the input size
to ensure it is a non-negative integer.
"""


class Square:
    """Represents a square with a validated size.

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
