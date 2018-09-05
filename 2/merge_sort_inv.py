"""
Implementation of merge sort that counts the number of inversions while
sorting.

An inversion for the array a is a pair (i, j) such that i < j and a[i] > a[j].

See problem 2-4
"""
from math import floor
from random import randint


def merge(arr, low, mid, high):
    """ assumes that arr[low:mid] and arr[mid:high] are sorted
        merges in place into arr[low:high]
        counts inversions missed by splitting array """
    n_left = mid - low
    n_right = high - mid
    inv_count = 0

    left = [0] * n_left
    right = [0] * n_right
    for i in range(n_left):
        left[i] = arr[low + i]
    for i in range(n_right):
        right[i] = arr[mid + i]

    i = j = k = 0
    while i < n_left and j < n_right:
        if left[i] <= right[j]:
            arr[low + k] = left[i]
            i += 1
        else:
            arr[low + k] = right[j]
            inv_count += n_left - i
            j += 1
        k += 1

    # if right runs out, merge remaining elements of left
    while i < n_left:
        arr[low + k] = left[i]
        i += 1
        k += 1

    # if left runs out, merge remaining elements of right
    while j < n_right:
        arr[low + k] = right[j]
        j += 1
        k += 1

    return inv_count


def merge_sort(arr, low, high):
    """ recursively sorts array by dividing and combining
        counts inversions in the unsorted array as it goes """
    inv_count = 0
    if low < high - 1:
        mid = floor((low + high) / 2)
        inv_count += merge_sort(arr, low, mid)
        inv_count += merge_sort(arr, mid, high)
        inv_count += merge(arr, low, mid, high)
    return inv_count


if __name__ == "__main__":
    rand_arr = [randint(0, 100) for _ in range(100)]
    count = merge_sort(rand_arr, 0, len(rand_arr))
    print(f"Input has {count} inversions.")
    print(rand_arr)
