"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Your runtime beats 78.18 % of python submissions.
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # #Method 1
        #         dict_diff = {}

        #         for elem in range(len(nums)):
        #             if nums[elem] in dict_diff:
        #                 return([elem, dict_diff[nums[elem]]])
        #             else:
        #                 dict_diff[target - nums[elem]] = elem
        #                 # print(dict_diff)

        # #Method 2
        # #Your runtime beats 78.18 % of python submissions.
        d = {}

        for i, j in enumerate(nums):
            if j in d:
                return [i, d[j]]
            else:
                d[target - j] = i