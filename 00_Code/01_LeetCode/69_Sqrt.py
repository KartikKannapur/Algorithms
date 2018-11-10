# #Implement int sqrt(int x).
# #Compute and return the square root of x.
# #x is guaranteed to be a non-negative integer.
# #Your runtime beats 81.07 % of python submissions.
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        """
        Method 1: Built-in functions
        """
        # import math
        # return int(math.sqrt(int(x)))

        """
        Method 2: Binary Search
        Your runtime beats 53.94 % of python submissions.
        """
        low = 0
        high = x

        while low <= high:
            mid = (low + high) // 2

            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid

            elif mid ** 2 > x:
                high = mid
            else:
                low = mid + 1