#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix
by a given divisor, with result rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divide each element of a matrix by div and round to 2 decimal places.

    Args:
        matrix: list of lists containing integers or floats.
        div: a number (int or float) that is not zero.

    Returns:
        A new matrix with each element divided by div.

    Raises:
        TypeError: If matrix is not a list of lists of numbers,
                   if rows have different lengths,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.

    Examples:
        >>> matrix = [[1, 2], [3, 4]]
        >>> matrix_divided(matrix, 2)
        [[0.5, 1.0], [1.5, 2.0]]
    """
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)
            or
            not all(isinstance(num, (int, float))
                    for row in matrix for num in row)):
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)

    if len({len(row) for row in matrix}) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
