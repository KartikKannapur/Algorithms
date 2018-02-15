"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Method 1: Naive Linear Search
        """
        #         var_min = nums[0]

        #         for i in range(0, len(nums)):
        #             if nums[i] < var_min:
        #                 var_min = nums[i]

        #         return(var_min)

        """
        Method 2: Binary Search
        Your runtime beats 10.53 % of python submissions
        """
        low = 0
        high = len(nums) - 1

        while low < high and nums[low] > nums[high]:
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]

