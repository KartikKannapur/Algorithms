"""
Description:

Count the number of prime numbers less than a non-negative number, n.

Your runtime beats 95.66 % of python submissions.
"""


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # #Using Sieve of Eratosthenes

        # #Method 1 - Memory Limit Exceed
        if n <= 2:
            return 0

        arr_flag = [1]*n

        for i in range(2, n):
            if arr_flag[i] == 1:
                for j in range(i+i, n, i):
                    arr_flag[j] = 0

        return sum(arr_flag)-2

        # #Method 2
        # #Your runtime beats 95.66 % of python submissions.
        if n <= 2:
            return 0

        arr_flag = [1] * n

        for i in range(2, int(n ** 0.5) + 1):
            if arr_flag[i]:
                arr_flag[i * i: n: i] = [0] * len(arr_flag[i * i: n: i])
        return sum(arr_flag) - 2