#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 2, 3, 1]), 9)

    def test_max_at_middle(self):
        self.assertEqual(max_integer([1, 5, 3]), 5)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 9]), 9)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_mixed_signs(self):
        self.assertEqual(max_integer([-10, 0, 5, -20]), 5)

    def test_single_element(self):
        self.assertEqual(max_integer([42]), 42)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_all_same(self):
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.3, 0.8]), 2.3)

    def test_mixed_int_and_float(self):
        self.assertEqual(max_integer([1, 2.5, 3, 0.1]), 3)

    def test_string(self):
        self.assertEqual(max_integer("holberton"), "t")  # max by ASCII

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["a", "abc", "ab"]), "abc")

    def test_none_argument(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_list_with_none(self):
        with self.assertRaises(TypeError):
            max_integer([1, None, 2])
