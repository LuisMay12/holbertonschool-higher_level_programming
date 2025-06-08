#!/usr/bin/python3
"""
This module provides a function that converts a JSON string
into its corresponding Python object.
"""

import json


def from_json_string(my_str):
    """
    Converts a JSON string into a Python data structure.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The corresponding Python object (list, dict, etc.).
    """
    return json.loads(my_str)
