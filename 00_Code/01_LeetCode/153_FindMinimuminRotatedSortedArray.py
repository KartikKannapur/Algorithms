# #Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# #(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# #Find the minimum element.
# #You may assume no duplicate exists in the array.
# #Your runtime beats 95.93 % of python submissions.

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # #Naive Method
        var_min = nums[0]

        for i in range(0, len(nums)):
            if nums[i] < var_min:
                var_min = nums[i]

        return(var_min)

        # #Binary Search
        l = 0
        r = len(nums) - 1

        while l < r and nums[l] > nums[r]:
            mid = l + (r - l) / 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]