#!/usr/bin/python3
"""
This module provides a function that reads and prints the content
of a UTF-8 text file to the standard output.
"""


def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints its content to stdout.
    The file is opened using a `with` statement for proper resource handling.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
