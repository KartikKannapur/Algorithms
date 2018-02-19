"""
Given an integer, write a function to determine if it is a power of two
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """
        Method 1: Repeated Division
        """
        #         while n % 2 == 0:
        #             n = n // 2

        #         if n == 1: return True
        #         else: return False


        """
        Method 2: !(n&(n-1))
        Your runtime beats 32.94 % of python submissions.
        """
        # if n > 0: return not(n&(n - 1))
        # else: return False

        # #Golfing
        return n > 0 and not (n & (n - 1))

