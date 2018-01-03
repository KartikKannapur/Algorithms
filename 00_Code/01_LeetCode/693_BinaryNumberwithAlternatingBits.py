# #Given a positive integer, check whether it has alternating bits:
# #namely, if two adjacent bits will always have different values.
# #Your runtime beats 59.69 % of python submissions.

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a = n ^ (n>>1)
        return a & (a+1) == 0