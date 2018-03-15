"""
A recursive implementation of insertion sort.
"""
from random import randint


def insertion_sort(arr, i):
    """
    Sort a list/array in place recursively using insertion sort.
    """
    if i > 1:
        insertion_sort(arr, i-1)
        key = arr[i-1]
        j = i - 2
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = key


if __name__ == "__main__":
    rand_arr = [randint(0, 1000) for _ in range(100)]
    insertion_sort(rand_arr, len(rand_arr))
    print(rand_arr)
