#!/usr/bin/python3
"""Module that defines a Square class with position and size validation.

Adds printing offset through position and allows full visual control
of how the square appears in the terminal.
"""


class Square:
    """Represents a square with size and position for printing.

    Attributes:
        __size (int): Length of the square's sides (must be >= 0).
        __position (tuple): Coordinates for offset (horizontal, vertical).
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with size and position.

        Args:
            size (int): Length of the square's sides.
            position (tuple): Tuple of 2 positive integers for offset.

        Raises:
            TypeError: If size is not an integer
            or position is not a valid tuple.
            ValueError: If size is negative.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the current size of the square.

        Returns:
            int: The size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the square's size with validation.

        Args:
            value (int): Size of the square.

        Raises:
            TypeError: If not an integer.
            ValueError: If less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square.

        Returns:
            tuple: The position (x, y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the square's position with validation.

        Args:
            value (tuple): Tuple of 2 positive integers.

        Raises:
            TypeError: If not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' characters, respecting position.

        If size is 0, prints an empty line. Horizontal and vertical offsets
        are applied using spaces and newlines respectively.
        """
        if self.__size == 0:
            print()
            return

        # Apply vertical offset
        for _ in range(self.__position[1]):
            print()

        # Print square with horizontal offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
