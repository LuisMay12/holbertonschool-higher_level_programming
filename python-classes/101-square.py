#!/usr/bin/python3
"""Module that defines a Square class with printable behavior using __str__.
"""


class Square:
    """Represents a square with size and position for printing."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the square's size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the square's position with validation."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square."""
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

    def __str__(self):
        """Returns the square as a string for printing."""
        if self.__size == 0:
            return ""

        result = []
        # Add vertical offset
        result.append("\n" * self.__position[1])

        # Build each line with horizontal offset
        for _ in range(self.__size):
            line = " " * self.__position[0] + "#" * self.__size
            result.append(line)

        # Join lines into one string, stripping final newline if needed
        return "\n".join(line for line in result).rstrip()
