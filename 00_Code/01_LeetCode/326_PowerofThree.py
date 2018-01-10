"""
Given an integer, write a function to determine if it is a power of three.

Your runtime beats 47.23 % of python submissions.
"""


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0: return False

        while n % 3 == 0:
            n /= 3
        if n == 1:
            return True
        else:
            return False