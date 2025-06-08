#!/usr/bin/python3
"""
This module provides a function that writes a string to a UTF-8 text file
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF-8 encoded text file and returns
    the number of characters written.

    If the file exists, it will be overwritten.
    If the file doesn't exist, it will be created.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
