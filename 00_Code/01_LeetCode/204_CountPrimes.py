"""
Description:

Count the number of prime numbers less than a non-negative number, n.

Your runtime beats 95.66 % of python submissions.
"""


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        Method 1: Brute Force - TLE

        Method 2: Using Sieve of Eratosthenes
        * Iterate from 2 to sqrt(n)+1
        * IF arr_flag[i] == 1, then for all multiples
        from i*i to n, in increments of i, we set 
        the elements of the flag array to be equal to zeo
        * Sum of 1's in the arr_flag minus 2 elements

        Your runtime beats 51.42 % of python3 submissions.
        """
        if n <= 2:
            return 0

        # #Flag matrix
        arr_flag = [1] * n

        for i in range(2, int(n ** 0.5) + 1):
            if arr_flag[i]:
                for j in range(i * i, n, i):
                    arr_flag[j] = 0

        return sum(arr_flag) - 2