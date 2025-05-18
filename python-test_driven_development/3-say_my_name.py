#!/usr/bin/python3
"""
This module defines a function that prints a full name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>"

    Args:
        first_name (str): The first name.
        last_name (str): The last name (optional, defaults to empty string).

    Raises:
        TypeError: If first_name or last_name is not a string.

    Examples:
        >>> say_my_name("John", "Smith")
        My name is John Smith
        >>> say_my_name("Bob")
        My name is Bob
        >>> say_my_name(12, "Smith")
        Traceback (most recent call last):
        TypeError: first_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
