#!/usr/bin/python3
"""This module defines a function that checks if an object is
exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class
        (not subclass), False otherwise.
    """
    return type(obj) is a_class
