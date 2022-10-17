#!/bin/python3
"""
    My addition Module
"""


def add_integer(a, b=98):
    """Args:
        a(int): first integer
        b(int):second integer
    Returns:
        Sum of two integers if successful
    Raises:
        TypeError: if a or b is not an integer."""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
