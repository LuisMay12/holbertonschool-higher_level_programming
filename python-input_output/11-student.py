#!/usr/bin/python3
"""
This module defines the Student class with methods
for JSON serialization and deserialization.
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
            dict: Dictionary of filtered or full attributes.
        """
        if type(attrs) is list and all(type(attr) is str for attr in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using a dictionary.

        Args:
            json (dict): A dictionary with keys as attribute names
                         and values as new values for the instance.
        """
        for key in json:
            setattr(self, key, json[key])
