#!/usr/bin/python3
"""
This module provides a function to calculate the weighted average
of all tuples in a list.
"""


def weight_average(my_list=[]):
    """
    Returns the weighted average of all integer tuples (score, weight).

    Args:
        my_list: List of tuples, where each tuple is (score, weight)

    Returns:
        The weighted average as a float, or 0 if the list is empty.
    """
    if not my_list:
        return 0

    total_weighted = 0
    total_weight = 0

    for score, weight in my_list:
        total_weighted += score * weight
        total_weight += weight

    return total_weighted / total_weight
