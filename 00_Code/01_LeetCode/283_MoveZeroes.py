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
        # #Method 1:
        # for i in range(0,len(nums)-1):
        #     if nums[i] == 0:
        #         for j in range(i,len(nums)):
        #             if nums[j] != 0:
        #                 break
        #         nums[i], nums[j] = nums[j], nums[i]

        # #Method 2:
        # zero_count = nums.count(0)
        # [nums.remove(0) for _ in range(zero_count)]
        # for _ in range(zero_count):
        #     nums.append(0)

        """
        Method 3:
        Your runtime beats 21.68 % of python submissions.
        """
        # for _ in range(nums.count(0)):
        #     nums.remove(0)
        #     nums.append(0)

        """
        Method 4:
        Create an array that keeps a track of the non-zero elements
        Create a counter that counts the number of zeros
        Combine the array and [0]*zero_counter
        But, this method is space sub-optimal

        Your runtime beats 89.72 % of python submissions.
        """
        arr_nonzero = []
        zero_counter = 0

        for ele in nums:
            if ele != 0:
                arr_nonzero.append(ele)
            else:
                zero_counter += 1
        nums[:] = arr_nonzero + [0] * zero_counter

