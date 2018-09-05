"""
Implementation of bubble sort. See problem 2-2
"""
from random import randint


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i - 1, -1):
            if arr[j - 1] > arr[j]:
                tmp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = tmp


if __name__ == "__main__":
    arr = [randint(0, 100) for _ in range(100)]
    bubble_sort(arr)
    print(arr)
