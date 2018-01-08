"""
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Runtime: 42 ms
"""


class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        Method 1
        Using Python built-in functions
        """
        if len(nums) > 1:
            arr = sorted(nums, reverse=True)
            if arr[0] >= 2*arr[1]: return nums.index(arr[0])
            else: return -1
        return 0

        """
        Method 2
        """
        max_one = max_two = float("-inf")
        max_index = 0

        if len(nums) > 1:
            for elem in range(0, len(nums)):
                if nums[elem] > max_one:
                    max_two = max_one
                    max_one = nums[elem]
                    max_index = elem

                if max_one > nums[elem] > max_two:
                    max_two = nums[elem]

            if max_one >= 2 * max_two:
                return max_index
            else:
                return -1

        else:
            return 0
