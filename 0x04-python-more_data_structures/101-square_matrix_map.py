#!/usr/bin/pytjon3
def square_matrix_map(matrix=[]):
    return list(map(lambda sublist: list(map(lambda num: num ** 2, sublist)), matrix))
