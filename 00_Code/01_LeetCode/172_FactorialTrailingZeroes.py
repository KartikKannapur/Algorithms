"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        Method 1:
        n/5 + n/25 + n/125 + n/625 ...

        Your runtime beats 40.59 % of python submissions.
        """
        counter = 0;

        while n:
            n = n // 5
            counter += n
        return counter