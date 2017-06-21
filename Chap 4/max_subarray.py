# max_subarray.py
from numpy.random import randint
from math import inf, floor
import sys


def max_crossing_subarray(arr, low, mid, high):
    """ find sub-array of arr[low:high] of form arr[i:j]
        where i < mid < j"""
    left_sum = -inf
    cur_sum = 0
    max_left = mid
    for i in range(mid-1, low-1, -1):
        cur_sum += arr[i]
        if cur_sum > left_sum:
            left_sum = cur_sum
            max_left = i
    right_sum = -inf
    cur_sum = 0
    max_right = mid
    for j in range(mid, high):
        cur_sum += arr[j]
        if cur_sum > right_sum:
            right_sum = cur_sum
            max_right = j + 1
    return max_left, max_right, left_sum + right_sum


def max_subarray(arr, low, high):
    """ find subarray of arr[low:high] with max sum """
    if low + 1 == high:
        return low, high, arr[low]
    else:
        mid = floor((high + low) / 2)
        left_low, left_high, left_sum = max_subarray(arr, low, mid)
        right_low, right_high, right_sum = max_subarray(arr, mid, high)
        cross_low, cross_high, cross_sum = max_crossing_subarray(arr, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


if __name__ == "__main__":
    n = 10
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    rand_arr = randint(-10, 10, n)
    left, right, best = max_subarray(rand_arr, 0, len(rand_arr))
    print(rand_arr)
    print("Left: {}, right: {}, sum: {}".format(left, right, best))
    print(rand_arr[left:right])
