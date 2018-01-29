"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        Method 1
        Your runtime beats 44.50 % of python submissions.
        """
        d ={}
        for i in range(0, len(nums)):
            if nums[i] in d:
                del d[nums[i]]
            else:
                d[nums[i]] = 1

        return d.keys()
