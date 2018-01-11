"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

Your runtime beats 77.91 % of python submissions.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = float("-Inf")
        max_ending_here = 0

        for i in range(0, len(nums)):
            max_ending_here += nums[i]

            if max_ending_here > max_so_far:
                max_so_far = max_ending_here

            if max_ending_here < 0:
                max_ending_here = 0

        return max_so_far