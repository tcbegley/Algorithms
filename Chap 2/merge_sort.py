# merge_sort.py
from math import inf, floor
from numpy.random import randint


def merge(arr, p, q, r):
    """ assumes that arr[p:q] and arr[q:r] are sorted
        merges in place into arr[p:r] """
    n1 = q - p
    n2 = r - q
    left = [0] * (n1 + 1)
    right = [0] * (n2 + 1)
    for i in range(n1):
        left[i] = arr[p+i]
    for i in range(n2):
        right[i] = arr[q+i]
    left[n1] = inf
    right[n2] = inf
    i = 0
    j = 0
    for k in range(p, r):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1


def merge_sort(arr, p, r):
    """ sort array in place using merge sort """
    if p < r - 1:
        q = floor((p + r) / 2)
        merge_sort(arr, p, q)
        merge_sort(arr, q, r)
        merge(arr, p, q, r)


if __name__ == "__main__":
    rand_arr = randint(0, 100, 100)
    merge_sort(rand_arr, 0, len(rand_arr))
    print(rand_arr)
