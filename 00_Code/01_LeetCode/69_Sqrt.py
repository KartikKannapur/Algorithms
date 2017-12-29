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
        import math
        return int(math.sqrt(int(x)))