#!/usr/bin/python3
"""Module that defines a Rectangle class with instance tracking.

Tracks the number of active Rectangle instances
and prints a goodbye message on deletion.
"""


class Rectangle:
    """Represents a rectangle with width, height, and instance tracking.

    Attributes:
        number_of_instances (int): Public class attribute to count instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle.

        Returns:
            int: The current width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width with validation.

        Args:
            value (int): New width.

        Raises:
            TypeError: If not an integer.
            ValueError: If less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle.

        Returns:
            int: The current height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height with validation.

        Args:
            value (int): New height.

        Raises:
            TypeError: If not an integer.
            ValueError: If less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle.

        Returns:
            int: Area (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle.

        Returns:
            int: Perimeter, or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string that visually represents the rectangle using '#'.

        Returns:
            str: Visual rectangle or empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Returns a string representation that can recreate the rectangle.

        Returns:
            str: In the format Rectangle(width, height).
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Called when the instance is deleted.

        Prints a goodbye message and decreases instance counter.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
