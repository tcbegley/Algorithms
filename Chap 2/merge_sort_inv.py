# merge_sort_inv.py
# merge sort with inversion counter
from numpy.random import randint
from math import floor


def merge(arr, p, q, r):
    """ assumes that arr[p:q] and arr[q:r] are sorted
        merges in place into arr[p:r]
        counts inversions missed by splitting array """
    n1 = q - p
    n2 = r - q
    inv_count = 0

    left = [0] * n1
    right = [0] * n2
    for i in range(n1):
        left[i] = arr[p+i]
    for i in range(n2):
        right[i] = arr[q+i]

    i = j = k = 0
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[p + k] = left[i]
            i += 1
        else:
            arr[p + k] = right[j]
            inv_count += n1 - i
            j += 1
        k += 1

    # if right runs out, merge remaining elements of left
    while i < n1:
        arr[p + k] = left[i]
        i += 1
        k += 1

    # if left runs out, merge remaining elements of right
    while j < n2:
        arr[p + k] = right[j]
        j += 1
        k += 1

    return inv_count


def merge_sort(arr, p, r):
    """ recursively sorts array by dividing and combining
        counts inversions in the unsorted array as it goes """
    inv_count = 0
    if p < r - 1:
        q = floor((p + r) / 2)
        inv_count += merge_sort(arr, p, q)
        inv_count += merge_sort(arr, q, r)
        inv_count += merge(arr, p, q, r)
    return inv_count


if __name__ == "__main__":
    rand_arr = randint(0, 100, 100)
    count = merge_sort(rand_arr, 0, len(rand_arr))
    print(count, '\n', rand_arr)
