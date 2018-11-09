"""
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

Your runtime beats 63.36 % of python submissions
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        Method 1: Binary Search for LOW + Binary Search for HIGH

        Your runtime beats 92.42 % of python submissions.
        """

        # #Binary Search to find LOW
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        # print(low, high)
        res1 = low

        # #Binary Search to find HIGH
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        # print(low, high)
        res2 = high

        # #Sanity Check
        if res1 <= res2:
            return [res1, res2]
        else:
            return [-1, -1]





