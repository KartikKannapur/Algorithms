"""
https://www.hackerrank.com/challenges/fibonacci-modified/problem
"""

# !/bin/python3

import sys


def fibonacciModified(t1, t2, n):
    # Complete this function
    memo = [0] * (n + 1)
    memo[0] = t1
    memo[1] = t2

    for i in range(2, n + 1):
        memo[i] = memo[i - 2] + (memo[i - 1] ** 2)

    return memo[n - 1]


if __name__ == "__main__":
    t1, t2, n = input().strip().split(' ')
    t1, t2, n = [int(t1), int(t2), int(n)]
    result = fibonacciModified(t1, t2, n)
    print(result)
