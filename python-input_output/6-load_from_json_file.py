#!/usr/bin/python3
"""
This module provides a function that creates a Python object
from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Loads a Python object from a file containing JSON content.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        object: The corresponding Python object (list, dict, etc.).
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
