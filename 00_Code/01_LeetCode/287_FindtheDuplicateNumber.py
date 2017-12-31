# #Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
# #Note:
# #You must not modify the array (assume the array is read only).
# #You must use only constant, O(1) extra space.
# #Your runtime complexity should be less than O(n2).
# #There is only one duplicate number in the array, but it could be repeated more than once.
# #Your runtime beats 73.24 % of python submissions.

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Method 1: Naive Solution
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return nums[j]

        # #Method 2: Sorting
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

        d = {}
        for i in range(0, len(nums)):
            if nums[i] in d:
                return nums[i]
            else:
                d[nums[i]] = i




