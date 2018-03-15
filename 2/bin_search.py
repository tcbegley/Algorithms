"""
Implementation of binary search. Exercise 2.3-5
"""
from random import randint


def bin_search(arr, low, high, key):
    """ search arr[low:high] for key using binary search """
    if low < high:
        q = (low + high) // 2
        if arr[q] == key:
            return q
        elif arr[q] > key:
            return bin_search(arr, low, q, key)
        else:
            return bin_search(arr, q+1, high, key)
    return -1


if __name__ == "__main__":
    rand_arr = [randint(0, 99) for _ in range(100)]
    rand_arr.sort()
    rand_key = randint(0, 99)
    idx = bin_search(rand_arr, 0, len(rand_arr), rand_key)
    if idx >= 0:
        print(f"{rand_key} found at index {idx}.")
    else:
        print(f"{rand_key} not found.")
