#!/bin/python3
""" MY module that prints a square"""


def print_square(size):
    """ prints a square
    Args:
        size(int): size of square
    Returns:
        nothing
    Raises:
        TypeError:
        ValueError:
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) or size < 0:
        raise TypeError("size must be an integer")
    for val in range(size):
        print("#" * size)
