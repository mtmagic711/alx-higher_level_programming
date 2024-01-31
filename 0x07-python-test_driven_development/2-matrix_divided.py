#!/usr/bin/python3

"""A function that divid all the elements of matrix by a number"""


def matrix_divided(matrix, div):
    """The function expects a list of lists and a number different from zero.

    Args:
        Arg1: the matrix.
        Arg2: the number to divide by.

    Returns:
        A new matrix.
    """

    if not all(
        isinstance(row, list) and
        all(isinstance(elem, (int, float)) for elem in row)
        for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
