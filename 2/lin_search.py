# lin_search.py
from numpy.random import randint


def lin_search(arr, key):
    """ search arr for key and return index of first match if found
        return -1 if not found """
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


if __name__ == "__main__":
    rand_arr = randint(0, 100, 100)
    rand_key = randint(0, 100, 1)[0]
    idx = lin_search(rand_arr, rand_key)
    if idx >= 0:
        print("{} found at index {}.".format(rand_key, idx))
    else:
        print("{} not found in array.".format(rand_key))
