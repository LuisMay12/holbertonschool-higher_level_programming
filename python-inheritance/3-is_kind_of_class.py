#!/usr/bin/python3
"""This module defines a function that checks if an object is
an instance of a class or its subclasses.
"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of a_class or any class inherited from it.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or
        its subclass, False otherwise.
    """
    return isinstance(obj, a_class)
