#!/usr/bin/python3
"""MyInt is a rebel that inverts == and !="""


class MyInt(int):
    """A subclass of int that inverts equality operators"""

    def __eq__(self, other):
        """Inverts the behavior of == (equality)"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the behavior of != (inequality)"""
        return super().__eq__(other)
