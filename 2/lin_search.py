"""
Linear search implementation. Exercise 2.1-3
"""
from numpy.random import randint


def lin_search(arr, key):
    """ search arr for key and return index of first match if found
        return -1 if not found """
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


if __name__ == "__main__":
    rand_arr = [randint(1, 100) for _ in range(100)]
    rand_key = randint(1, 100)
    idx = lin_search(rand_arr, rand_key)
    if idx >= 0:
        print(f"{rand_key} found at index {idx}.")
    else:
        print(f"{rand_key} not found in array.")
