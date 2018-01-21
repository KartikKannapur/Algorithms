"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Your runtime beats 48.41 % of python submissions
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # #Special Case
        if len(nums) < 3: return []

        if len(nums) == 3:
            if sum(nums) == 0:
                return [sorted(nums)]

        # #General Case
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            low = i + 1
            high = len(nums) - 1

            # #To handle Time Limit Exceeded Error
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            while low < high:
                temp_sum = nums[i] + nums[low] + nums[high]
                if temp_sum == 0:
                    res.append((nums[i], nums[low], nums[high]))

                if temp_sum > 0:
                    high -= 1
                else:
                    low += 1

        # #Return unique elements
        return list(set(tuple(res)))