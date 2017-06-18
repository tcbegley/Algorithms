# merge_sort2.py
# alternative implementation of merge sort not using 'sentinels'
from numpy.random import randint
from math import floor


def merge(arr, p, q, r):
    """ assumes that arr[p:q] and arr[q:r] are sorted
        merges in place into arr[p:r] """
    n1 = q - p
    n2 = r - q

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
            j += 1
        k += 1

    # if right runs out, merge remaining elements of left
    while i < n1:
        arr[p + k] = left[i]
        i += 1
        k += 1

    # if left runs out, merge remeining elements of right
    while j < n2:
        arr[p + k] = right[j]
        j += 1
        k += 1


def merge_sort(arr, p, r):
    """ recursively applies merge_sort to sub arrays then merges """
    if p < r - 1:
        q = floor((p + r) / 2)
        merge_sort(arr, p, q)
        merge_sort(arr, q, r)
        merge(arr, p, q, r)


if __name__ == "__main__":
    rand_arr = randint(0, 100, 100)
    merge_sort(rand_arr, 0, len(rand_arr))
    print(rand_arr)
