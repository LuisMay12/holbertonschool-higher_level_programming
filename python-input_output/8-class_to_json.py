#!/usr/bin/python3
"""
This module provides a function that returns the dictionary
description of a simple Python object for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a class with serializable
        attributes (str, int, bool, list, dict).

    Returns:
        dict: A dictionary representation of the object.
    """
    return obj.__dict__
