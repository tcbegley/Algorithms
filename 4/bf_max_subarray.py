# bf_max_subarray.py
# this is a brute force solution of the max_subarray problem
from numpy.random import randint
from math import inf
import sys


def max_subarray(arr):
    """ find sub-array of arr with largest sum """
    best_sum = -inf
    best_low = 0
    best_high = 0
    for i in range(len(arr)):
        cur_sum = 0
        for j in range(i, len(arr)):
            cur_sum += arr[j]
            if cur_sum > best_sum:
                best_low = i
                best_high = j + 1
                best_sum = cur_sum
    return best_low, best_high, best_sum


if __name__ == "__main__":
    n = 10
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    rand_arr = randint(-10, 10, n)
    left, right, best = max_subarray(rand_arr)
    print(rand_arr)
    print("Low: {}, high: {}, sum: {}".format(left, right, best))
    print(rand_arr[left:right])
