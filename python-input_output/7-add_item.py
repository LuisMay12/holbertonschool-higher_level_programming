#!/usr/bin/python3
"""
This script adds command-line arguments to a list and saves them
in a JSON file named add_item.json. If the file exists, it loads
the list first, otherwise it starts with an empty list.
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except Exception:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, filename)
