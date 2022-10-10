#!/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    if len(matrix) == 0 or not matrix:
        return None
    for val in matrix:
        new_matrix.append(list(map(lambda a: a * a, val)))
    return new_matrix
