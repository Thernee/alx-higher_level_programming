#!/usr/bin/python3
"""A function for matrix multiplication"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using numpy."""
    result = np.matmul(m_a, m_b)
    return result
