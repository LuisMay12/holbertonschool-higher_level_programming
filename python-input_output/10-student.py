#!/usr/bin/python3
"""
This module defines the Student class with a method that can
filter its dictionary representation based on a list of attributes.
"""


class Student:
    """
    Represents a student with a first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictionary representation of the Student instance.
        If attrs is a list of strings, only those attributes are included.

        Args:
            attrs (list): Optional list of attribute names to include.

        Returns:
            dict: Filtered or full dictionary of attributes.
        """
        if type(attrs) is list and all(type(attr) is str for attr in attrs):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__
