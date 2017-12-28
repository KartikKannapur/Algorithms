# #Given an array and a value, remove all instances of that value in-place and return the new length.
# #Your runtime beats 64.83 % of python submissions

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # #Method 1
        my_nums = nums[:]
        for ele in my_nums:
            if ele == val:
                nums.remove(ele)

        # #Method 2
        while val in nums:
            nums.remove(val)

