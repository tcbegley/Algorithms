"""
Implementation of selection sort. Exercise 2.2-2
"""
from random import randint


def selection_sort(arr):
    """ sort a list/array in place using selection sort """
    for i in range(len(arr)-1):
        min_i = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j
        temp = arr[i]
        arr[i] = arr[min_i]
        arr[min_i] = temp


if __name__ == "__main__":
    rand_arr = [randint(0, 100) for _ in range(100)]
    selection_sort(rand_arr)
    print(rand_arr)
