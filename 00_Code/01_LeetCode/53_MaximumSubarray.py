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

        """
        Method 1: Using two for loops - Complexity O(n^2)
        """

        """
        Method 2: Dynamic Programming

        * Keep two variables max_res and max_here
        max_res is the overall maximum and max_here
        is the maxium value until that point in the
        loop

        * Constantly keep updating max_here and max_res

        Your runtime beats 88.98 % of python submissions.
        """

        max_res = float("-Inf")
        max_here = 0

        for i in range(0, len(nums)):
            max_here += nums[i]

            if max_here > max_res:
                max_res = max_here

            if max_here < 0:
                max_here = 0

        return max_res