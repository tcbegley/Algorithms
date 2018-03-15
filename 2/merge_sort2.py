"""
Alternative implementation of merge sort not using 'sentinels' (i.e. inf).

Exercise 2.3-2
"""
from math import floor
from random import randint


def merge(arr, low, mid, high):
    """
    Assumes that arr[low:mid] and arr[mid:high] are sorted
    merges in place into arr[low:high]
    """
    n_left = mid - low
    n_right = high - mid

    left = [0] * n_left
    right = [0] * n_right
    for i in range(n_left):
        left[i] = arr[low+i]
    for i in range(n_right):
        right[i] = arr[mid+i]

    i = j = k = 0
    while i < n_left and j < n_right:
        if left[i] <= right[j]:
            arr[low + k] = left[i]
            i += 1
        else:
            arr[low + k] = right[j]
            j += 1
        k += 1

    # if right runs out, merge remaining elements of left
    while i < n_left:
        arr[low + k] = left[i]
        i += 1
        k += 1

    # if left runs out, merge remeining elements of right
    while j < n_right:
        arr[low + k] = right[j]
        j += 1
        k += 1


def merge_sort(arr, low, high):
    """ recursively applies merge_sort to sub arrays then merges """
    if low < high - 1:
        mid = floor((low + high) / 2)
        merge_sort(arr, low, mid)
        merge_sort(arr, mid, high)
        merge(arr, low, mid, high)


if __name__ == "__main__":
    rand_arr = [randint(0, 100) for _ in range(100)]
    merge_sort(rand_arr, 0, len(rand_arr))
    print(rand_arr)
