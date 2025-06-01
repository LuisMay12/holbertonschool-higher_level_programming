#!/usr/bin/python3
"""Function to add an attribute to an object if possible."""


def add_attribute(obj, name, value):
    """Add a new attribute to an object if it's allowed.

    Args:
        obj: The object to which the attribute will be added.
        name: The name of the attribute to add.
        value: The value to set for the attribute.

    Raises:
        TypeError: If the attribute can't be added.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
