#!/usr/bin/python3
"""
This module provides functions to serialize and deserialize
Python dictionaries using XML format.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the file to save the XML content.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a Python dictionary.

    Args:
        filename (str): The XML file to read and parse.

    Returns:
        dict: A dictionary with the parsed data.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for element in root:
        result[element.tag] = element.text

    return result
