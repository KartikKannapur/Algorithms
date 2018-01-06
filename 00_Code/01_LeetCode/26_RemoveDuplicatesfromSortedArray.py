"""
Given a sorted array, remove the duplicates in-place
such that each element appear only once and return the
new length.

Do not allocate extra space for another array, you must
do this by modifying the input array in-place with O(1)
extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first
two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.

Your runtime beats 25.22 % of python submissions
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # #Method 1:
        return len([nums[i] for i in range(0, len(nums)) if i == len(nums)-1 or nums[i+1] != nums[i]])

        # #Method 2:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
        return len(nums)

