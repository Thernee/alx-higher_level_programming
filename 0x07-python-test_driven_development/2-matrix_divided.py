#!/usr/bin/python3

"""
Define matrix_divided function
Takes 2 arguments (matrix and div)
Returns: new_matrix if successful, raises error otherwise
"""


def matrix_divided(matrix, div):
    """
    Divide elements of a matrix
    """
    if type(div) not in (int, float):
        raise TypeError("div must be an integer")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    err = "matrix must be a matrix (list of lists) of integers/floats"
    row_len = len(matrix)
    col_len = len(matrix[0])
    new_matrix = [[0.0] * col_len for _ in range(row_len)]

    for num in range(len(matrix)):
        if len(matrix[0]) != len(matrix[num]):
            raise TypeError("Each row of the matrix must have the same size")
        for i in range(len(matrix[0])):
            if type(matrix[num][i]) not in (int, float):
                raise TypeError(err)
            new_matrix[num][i] = round(matrix[num][i]/div, 2)
    return new_matrix
