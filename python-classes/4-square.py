#!/usr/bin/python3
"""Module that defines a Square class with getter and setter for size.

This module adds controlled access to the private attribute `__size`
using property decorators, and includes validation during updates.
"""


class Square:
    """Represents a square with a size that can be safely accessed and updated.

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
        self.size = size  # Calls the setter for validation

    @property
    def size(self):
        """Gets the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area (size * size).
        """
        return self.__size ** 2
