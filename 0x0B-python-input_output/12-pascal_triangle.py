#!/usr/bin/python3

"""Pascal Triangle Module/ Function"""


def pascal_triangle(n):
    """Prints Pascal Triangle"""
    if n <= 0:
        return []

    triangle = [[1]]

    for _ in range(1, n):
        next_row = []
        row_calc = [0] + triangle[-1] + [0]

        for i in range(len(triangle[-1]) + 1):
            next_row.append(row_calc[i] + row_calc[i + 1])
        triangle.append(next_row)

    return triangle
