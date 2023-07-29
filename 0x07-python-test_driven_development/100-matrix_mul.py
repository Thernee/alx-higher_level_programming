#!/usr/bin/python3
"""A function for matrix multiplication"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices."""

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if all([not isinstance(ele, int) and not isinstance(ele, float)
            for row in m_a for ele in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not any([isinstance(ele, int) or isinstance(ele, float)
                for row in m_b for ele in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    invert_val = []
    for row in range(len(m_b[0])):
        new_row = []
        for col in range(len(m_b)):
            new_row.append(m_b[col][row])
        invert_val.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in invert_val:
            product = 0
            for x in range(len(invert_val[0])):
                product += row[x] * col[x]
            new_row.append(product)
        new_matrix.append(new_row)

    return new_matrix
