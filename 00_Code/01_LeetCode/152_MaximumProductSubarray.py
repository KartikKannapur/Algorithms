"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

Your runtime beats 74.84 % of python submissions
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = neg = max_prod = nums[0]

        for n in nums[1:]:
            if n <= 0:
                neg, pos = (min(n, pos * n), neg * n)
            else:
                neg, pos = (neg * n, max(n, pos * n))

            max_prod = max(max_prod, pos)

        return max_prod

