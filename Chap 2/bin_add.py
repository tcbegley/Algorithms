# bin_add.py
from numpy.random import randint


# helper functions for converting to and from binary arrays
def to_bin(n):
    arr = []
    while n:
        arr.append(n)
        n //= 2
    return arr


def to_int(arr):
    n = 0
    power = 1
    for i in arr:
        n += i*power
        power *= 2
    return n


def bin_add(a, b):
    if len(a) != len(b):
        raise ValueError("Binary arrays must have same length.")

    carry = False

    for i in range(len(a)):
        x = a[i] + b[i]
        if carry:
            x += 1
        yield x % 2
        carry = x > 1
    if carry:
        # allow for overflow from addition
        yield 1


if __name__ == "__main__":
    # ensure that binary representations of numbers to be added have same length
    n1, n2 = randint(64, 128, 2)
    n3 = to_int(list(bin_add(list(to_bin(n1)), list(to_bin(n2)))))
    print("The sum of {} and {} is {}".format(n1, n2, n3))
