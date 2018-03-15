#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy.random import randint


# helper functions for converting to and from binary arrays
def to_bin(n):
    """ convert non-negative integer n to binary array """
    arr = []
    while n:
        arr.append(n % 2)
        n //= 2
    return arr


def to_int(arr):
    """ convert binary array to integer """
    n = 0
    power = 1
    for i in arr:
        n += i*power
        power *= 2
    return n


def bin_add(a, b):
    """ add two binary arrays of same length """
    if len(a) != len(b):
        raise ValueError("Binary arrays must have same length.")

    c = [0] * len(a)
    carry = False

    for i in range(len(a)):
        x = a[i] + b[i]
        if carry:
            x += 1
        c[i] = x % 2
        carry = x > 1
    if carry:
        # allow for overflow from addition
        c.append(1)
    return c


if __name__ == "__main__":
    n1, n2 = randint(64, 128, 2)
    n3 = to_int(bin_add(to_bin(n1), to_bin(n2)))
    print("The sum of {} and {} is {}".format(n1, n2, n3))