#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix:
        length = len(matrix)
        new_matrix = []

        for element in matrix:
            new_element = [x**2 for x in element]
            new_matrix.append(new_element)
        return new_matrix
