# #Implement pow(x, n)
# #Your runtime beats 81.35 % of python submissions.


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # #Method 1:
        import math
        return math.pow(x, n)

        # #Method 2:
        return pow(x, n)