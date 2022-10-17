#!/bin/python3
"""
My Module on Matrix division
"""


def matrix_divided(matrix, div):
    """ Function that divides a matrix integer by div
    Args:
        matrix(list): list of lists
        div(int): integer used for division
    Returns:
        A Matrix if successful
    Raises:
        TypeError: must be a list of lists with int or float
        ZeroDivisionError: div must not be zero
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or  # comprehension for rows
            not all(((isinstance(ele, int) or isinstance(ele, float))
                     for ele in [num for row in matrix for num in row]))):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]  # new_matrix
