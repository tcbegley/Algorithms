"""
Implementation of merge sort. Section 2.3.1
"""
from math import floor, inf
from random import randint


def merge(arr, low, mid, high):
    """
    Assumes that arr[low:mid] and arr[mid:high] are sorted merges in place
    into arr[low:high]
    """
    n_left = mid - low
    n_right = high - mid
    left = [0] * (n_left + 1)
    right = [0] * (n_right + 1)
    for i in range(n_left):
        left[i] = arr[low + i]
    for i in range(n_right):
        right[i] = arr[mid + i]
    left[n_left] = inf
    right[n_right] = inf
    i = 0
    j = 0
    for k in range(low, high):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1


def merge_sort(arr, low, high):
    """
    Sort array in place using merge sort.
    """
    if low < high - 1:
        mid = floor((low + high) / 2)
        merge_sort(arr, low, mid)
        merge_sort(arr, mid, high)
        merge(arr, low, mid, high)


if __name__ == "__main__":
    rand_arr = [randint(0, 100) for _ in range(100)]
    merge_sort(rand_arr, 0, len(rand_arr))
    print(rand_arr)
