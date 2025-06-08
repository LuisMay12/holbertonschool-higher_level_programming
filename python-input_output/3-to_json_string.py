#!/usr/bin/python3
"""
This module provides a function that returns the JSON
representation of a Python object as a string.
"""

import json


def to_json_string(my_obj):
    """
    Converts a Python object to a JSON string.

    Args:
        my_obj: The Python object to serialize.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
