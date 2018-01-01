# #You have a total of n coins that you want to form in a staircase shape,
# #where every k-th row must have exactly k coins.
# #Given n, find the total number of full staircase rows that can be formed.
# #n is a non-negative integer and fits within the range of a 32-bit signed integer.
# #Your runtime beats 84.49 % of python submissions.

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((-1 + (math.sqrt(1+8*n)))/2)