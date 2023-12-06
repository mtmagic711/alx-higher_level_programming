#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [list(row) for row in matrix]
    for row_i, row in enumerate(new_matrix):
        for row_j, elem in enumerate(row):
            new_matrix[row_i][row_j] = elem**2
    return new_matrix
