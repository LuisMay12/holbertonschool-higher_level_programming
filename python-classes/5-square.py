#!/usr/bin/python3
"""Module that defines a Square class with printing capability.

This module allows creation of square objects with a defined size,
supports size validation, computes area, and prints the square visually.
"""


class Square:
    """Represents a square with size validation and visual print.

    Attributes:
        __size (int): The size of the square, must be >= 0.
    """

    def __init__(self, size=0):
        """Initializes a Square instance with optional size.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # uses the setter

    @property
    def size(self):
        """Retrieves the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.

        Args:
            value (int): New size of the square.

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

    def my_print(self):
        """Prints the square using '#' characters.

        If size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
