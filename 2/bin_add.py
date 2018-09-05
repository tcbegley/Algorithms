"""
Addition function that takes input as binary arrays. Exercise 2.1-4
"""
from functools import reduce
from random import randint


def to_bin(n):
    """
    Convert non-negative integer n to binary array.
    """
    arr = []
    while n:
        arr.append(n % 2)
        n //= 2
    return arr


def to_int(arr):
    """
    Convert binary array to integer.
    """
    return reduce(lambda x, y: 2 * x + y, reversed(arr))


def bin_add(a, b):
    """
    Add two binary arrays of same length
    """
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
    n1, n2 = [randint(64, 127) for _ in range(2)]
    n3 = to_int(bin_add(to_bin(n1), to_bin(n2)))
    print(f"The sum of {n1} and {n2} is {n3}")
