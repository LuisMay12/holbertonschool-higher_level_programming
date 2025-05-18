#!/usr/bin/python3
"""
This module provides a function to add two integers.
It ensures the inputs are integers or floats,
casts floats to integers, and raises a TypeError
for invalid input types.
"""


def add_integer(a, b=98):
    """
    Add two integers or floats (which are casted to integers).

    Args:
        a: The first number (int or float).
        b: The second number (int or float), default is 98.

    Returns:
        The integer addition result of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.

    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2)
        100
        >>> add_integer(100.3, -2)
        98
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
