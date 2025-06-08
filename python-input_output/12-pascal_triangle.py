#!/usr/bin/python3
"""
This module provides a function to generate Pascal's Triangle
up to a given number of rows.
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle of size n.

    Args:
        n (int): The number of rows of the triangle to generate.

    Returns:
        list: A list of lists of integers representing Pascal’s triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
