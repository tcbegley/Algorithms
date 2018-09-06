"""
This is an implementation of Strassen's multiplication algorithm for square
matrices.
"""
from math import ceil, log2

import numpy as np


def strassen(a, b):
    """
    Multiply the matrices a and b together. Need not be square.
    """
    a_shape = a.shape
    b_shape = b.shape
    if a_shape[1] != b_shape[0]:
        raise ValueError(f"shapes {a_shape} and {b_shape} are not aligned")

    # set n to smallest power of two largest than any of the dimensions
    n = int(2 ** (ceil(log2(max(*a_shape, *b_shape)))))
    a_new = np.zeros((n, n))
    b_new = np.zeros((n, n))

    # pad original matrices with zeros to make them square
    a_new[: a_shape[0], : a_shape[1]] = a
    b_new[: b_shape[0], : b_shape[1]] = b

    return strassen_rec(a_new, b_new)[: a_shape[0], : b_shape[1]]


def strassen_rec(a, b):
    n = a.shape[0]
    if n == 1:
        return a * b

    c = np.zeros((n, n))

    a11 = a[: n // 2, : n // 2]
    a12 = a[: n // 2, n // 2 :]
    a21 = a[n // 2 :, : n // 2]
    a22 = a[n // 2 :, n // 2 :]
    b11 = b[: n // 2, : n // 2]
    b12 = b[: n // 2, n // 2 :]
    b21 = b[n // 2 :, : n // 2]
    b22 = b[n // 2 :, n // 2 :]

    s1 = b12 - b22
    s2 = a11 + a12
    s3 = a21 + a22
    s4 = b21 - b11
    s5 = a11 + a22
    s6 = b11 + b22
    s7 = a12 - a22
    s8 = b21 + b22
    s9 = a11 - a21
    s10 = b11 + b12

    p1 = strassen(a11, s1)
    p2 = strassen(s2, b22)
    p3 = strassen(s3, b11)
    p4 = strassen(a22, s4)
    p5 = strassen(s5, s6)
    p6 = strassen(s7, s8)
    p7 = strassen(s9, s10)

    c[: n // 2, : n // 2] = p4 + p5 + p6 - p2
    c[: n // 2, n // 2 :] = p1 + p2
    c[n // 2 :, : n // 2] = p3 + p4
    c[n // 2 :, n // 2 :] = p1 + p5 - p3 - p7

    return c
