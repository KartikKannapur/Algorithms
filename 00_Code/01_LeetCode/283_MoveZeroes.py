"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

Your runtime beats 14.22 % of python submissions.
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #Method 1:
        for i in range(0,len(nums)-1):
            if nums[i] == 0:
                for j in range(i,len(nums)):
                    if nums[j] != 0:
                        break
                nums[i], nums[j] = nums[j], nums[i]

        #Method 2:
        zero_count = nums.count(0)
        [nums.remove(0) for _ in range(zero_count)]
        for _ in range(zero_count):
            nums.append(0)

        # #Method 3:
        for _ in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)

