# bin_search.py
from numpy.random import randint
from math import floor


def bin_search(arr, p, r, key):
    """ search arr[p:r] for key using binary search """
    if p < r:
        q = floor((p + r) / 2)
        if arr[q] == key:
            return q
        elif arr[q] > key:
            return bin_search(arr, p, q, key)
        else:
            return bin_search(arr, q+1, r, key)
    return -1


if __name__ == "__main__":
    rand_arr = randint(0, 100, 100)
    rand_arr.sort()
    rand_key = randint(0, 100, 1)[0]
    idx = bin_search(rand_arr, 0, len(rand_arr), rand_key)
    if idx >= 0:
        print("{} found at index {}.".format(rand_key, idx))
    else:
        print("{} not found.".format(rand_key))
