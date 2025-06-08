#!/usr/bin/python3
"""
This module provides a function that writes a Python object
to a text file using its JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file using JSON representation.

    Args:
        my_obj: The object to be serialized and written.
        filename (str): The name of the file to write to.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
