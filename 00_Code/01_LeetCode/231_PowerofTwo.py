# #Given an integer, write a function to determine if it is a power of two
# #Your runtime beats 32.94 % of python submissions.

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # #Method 1
        while n % 2 == 0:
            n = n // 2

        if n == 1: return True
        else: return False

        # #Method 2
        if n > 1: return n and (not(n & (n - 1)))
        elif n == 1: return True
        else: return False

        # #Method 3
        if n > 0:
            return not (n & (n - 1))
        else:
            return False
