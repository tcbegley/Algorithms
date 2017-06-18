# insertion_sort.py
from numpy.random import randint


def insertion_sort(arr):
    """ sort a list/array in place using insertion sort """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while (j >= 0) and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


if __name__ == "__main__":
    rand_arr = list(randint(0, 1000, 100))
    insertion_sort(rand_arr)
    print(rand_arr)
