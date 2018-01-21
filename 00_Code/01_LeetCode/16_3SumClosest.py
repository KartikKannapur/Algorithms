"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


Your runtime beats 38.37 % of python submissions
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        Algo: Three Pointer Method
        Catch: check if abs(temp_sum - target) < abs(min_value-target)
        """
        # #Special Case
        if len(nums) < 3: return []

        if len(nums) == 3:
            return sum(nums)

        # #General Case
        nums.sort()
        min_value = sum(nums[:3])

        for i in range(len(nums) - 2):
            low = i + 1
            high = len(nums) - 1

            while low < high:
                temp_sum = nums[i] + nums[low] + nums[high]

                # #Case - Sum of the 3 numbers is equal to the target
                if temp_sum == target:
                    return temp_sum

                # #IMPORTANT CASE
                if abs(temp_sum - target) < abs(min_value - target):
                    min_value = temp_sum

                if temp_sum > target:
                    high -= 1
                elif temp_sum < target:
                    low += 1

        return min_value
