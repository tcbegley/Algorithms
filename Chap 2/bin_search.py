# bin_search.py
from numpy.random import randint
from math import floor


def bin_search(arr, low, high, key):
    """ search arr[low:high] for key using binary search """
    if low < high:
        q = floor((low + high) / 2)
        if arr[q] == key:
            return q
        elif arr[q] > key:
            return bin_search(arr, low, q, key)
        else:
            return bin_search(arr, q+1, high, key)
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
