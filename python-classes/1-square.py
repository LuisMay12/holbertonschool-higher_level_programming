#!/usr/bin/python3
"""Module that defines a class Square with a private size attribute.

This module introduces encapsulation by defining an instance variable
that is not accessible from outside the class directly.
"""


class Square:
    """Represents a square with a size.

    Attributes:
        __size (int): The size of the square, kept private.
    """

    def __init__(self, size):
        """Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square (no validation performed).
        """
        self.__size = size
