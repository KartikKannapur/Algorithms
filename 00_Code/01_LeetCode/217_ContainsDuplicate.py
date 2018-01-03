# #Given an array of integers, find if the array contains any duplicates.
# #Your function should return true if any value appears at least twice
# #in the array, and it should return false if every element is distinct.
# #Your runtime beats 54.14 % of python submissions.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # #Method 1:
        if nums:
            nums.sort()
            return len(nums) != len(list(set(nums)))
        return False

        # #Method 2:
        if nums:
            nums.sort()

            for i in range(1, len(nums)):
                if nums[i] == nums[i - 1]:
                    return True
        return False