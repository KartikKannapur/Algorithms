"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
"""


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """
        Method 1: Brute Force
        The algorithm works. But, produces a Time Limit Exceeded Error
        for large inputs
        """
        res = m
        ele = m+1

        while ele < n+1:
            res = res&ele
            ele += 1
            if res == 0:
                return 0

        return res

        """
        Method 2: Bit Manipulation
        Your runtime beats 62.55 % of python submissions
        """
        ele = 0
        while m != n:
            m >>= 1
            n >>= 1
            ele += 1
        return n << ele