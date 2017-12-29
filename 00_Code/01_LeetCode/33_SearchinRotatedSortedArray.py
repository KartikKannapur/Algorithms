# #Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# #(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# #You are given a target value to search. If found in the array return its index, otherwise return -1.
# #You may assume no duplicate exists in the array.
# #Your runtime beats 82.28 % of python submissions.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = int((l + r) / 2)
            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
