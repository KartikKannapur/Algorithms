"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 1:

Input: [1,3,5,6], 0
Output: 0

Your runtime beats 98.52 % of python submissions.
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # #Method 1: O(n)
        if target in nums:
            return(nums.index(target))
        else:
            for i in range(len(nums)):
                if nums[i] > target:
                    return i
                    # nums.insert(i, target)
                    # break
            return len(nums)

        # #Method 2: O(logn) - Binary Search
        # #Your runtime beats 98.52 % of python submissions.
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low
