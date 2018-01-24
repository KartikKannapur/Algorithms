"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

Your runtime beats 53.77 % of python submissions.
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Method 1: Simultaneous Assignment
        Your runtime beats 53.77 % of python submissions.

        Always conside (n, pos*n, neg*n)
        pos = max()
        neg = min()
        """
        pos = neg = max_prod = nums[0]
        for n in nums[1:]:
            pos, neg = max(n, n * pos, n * neg), min(n, n * pos, n * neg)
            max_prod = max(max_prod, pos)

        return max_prod
