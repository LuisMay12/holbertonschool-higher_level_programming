#!/usr/bin/python3
"""This module defines a subclass of list called MyList
with a method to print the list in sorted ascending order.
"""


class MyList(list):
    """MyList is a subclass of list with a custom method
    to print its elements sorted in ascending order.
    """

    def print_sorted(self):
        """Prints the list in ascending sorted order without
        changing the original list."""
        print(sorted(self))
