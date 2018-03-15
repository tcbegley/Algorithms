# insertion_sort_rec.py
# a recursive implementation of insertion sort
from numpy.random import randint


def insertion_sort(arr, i):
    """ sort a list/array in place recursively using insertion sort """
    if i > 1:
        insertion_sort(arr, i-1)
        key = arr[i-1]
        j = i - 2
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = key


if __name__ == "__main__":
    rand_arr = list(randint(0, 1000, 100))
    insertion_sort(rand_arr, len(rand_arr))
    print(rand_arr)
