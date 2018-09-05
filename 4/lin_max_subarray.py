"""
A linear time solution of the max subarray problem
"""
import sys
from math import inf

from numpy.random import randint


def max_subarray(arr):
    """ find subarray of arr with largest sum """
    best_sum = -inf
    best_left = 0
    best_right = 1
    cur_left = 0
    cur_sum = 0
    for i in range(len(arr)):
        if cur_sum >= 0:
            cur_sum += arr[i]
        else:
            cur_sum = arr[i]
            cur_left = i
        if cur_sum > best_sum:
            best_sum = cur_sum
            best_left = cur_left
            best_right = i + 1
    return best_left, best_right, best_sum


if __name__ == "__main__":
    n = 10
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    rand_arr = randint(-10, 10, n)
    left, right, best = max_subarray(rand_arr)
    print(rand_arr)
    print("Low: {}, high: {}, sum: {}".format(left, right, best))
    print(rand_arr[left:right])
