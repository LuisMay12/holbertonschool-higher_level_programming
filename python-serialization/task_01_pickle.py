#!/usr/bin/python3
"""
This module defines a custom class with serialization and
deserialization methods using the pickle module.
"""

import pickle


class CustomObject:
    """
    A custom Python class that represents a person or student.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Whether the person is a student.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes a new CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): True if the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the object's attributes in a formatted way.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current object and saves it to a file.

        Args:
            filename (str): The name of the file to write to.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            pass

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from a file and returns a new instance.

        Args:
            filename (str): The name of the file to read from.

        Returns:
            CustomObject | None: The deserialized object, or None on failure.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except Exception:
            return None
