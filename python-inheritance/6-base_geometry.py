#!/usr/bin/python3
"""Defines a class BaseGeometry with an area method."""


class BaseGeometry:
    """Base class for geometry-related calculations."""

    def area(self):
        """Raises an exception indicating that area() is not implemented."""
        raise Exception("area() is not implemented")
