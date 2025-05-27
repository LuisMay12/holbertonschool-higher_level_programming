#!/usr/bin/python3
"""This module defines a function that checks if an object is
an instance of a subclass of a specified class.
"""


def inherits_from(obj, a_class):
    """Checks if obj is an instance of a
    subclass of a_class (not a_class itself).

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is instance of a subclass
        of a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
