"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

Your runtime beats 50.00 % of python submissions.
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []

        for i in range(len(nums) - 3):
            # #To handle Time Limit Exceeded Error
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # #Create a sub-target
            target2 = target - nums[i]
            for j in range(i + 1, len(nums) - 2):

                # #To handle Time Limit Exceeded Error
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                low = j + 1
                high = len(nums) - 1

                # #Create a sub-target
                target3 = target2 - nums[j]

                while low < high:
                    sum_value = nums[low] + nums[high]

                    if sum_value == target3:
                        result.append([nums[i], nums[j], nums[low], nums[high]])

                        temp_low = nums[low]
                        low += 1

                        while low < high and nums[low] == temp_low:
                            low += 1

                        temp_high = nums[high]
                        high -= 1

                        while low < high and nums[high] == temp_high:
                            high -= 1

                    elif sum_value < target3:
                        low += 1
                    else:
                        high -= 1
        return result
