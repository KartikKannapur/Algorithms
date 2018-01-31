"""
Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
Note: Your solution should run in O(log n) time and O(1) space.
"""


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Method 1: Brute Force
        Method 2: Maintain a dict/Counter
        Method 3: append/pop or add and subtract from a variable

        Your runtime beats 48.96 % of python submissions.
        All these operations are O(n)
        """
        summer = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                summer += nums[i]
            else:
                summer -= nums[i]

        return (summer)

        """
        Method 4: Binary Search
        Your runtime beats 81.40 % of python submissions.
        """
        low = 0
        high = len(nums) - 1

        while (low < high):
            mid = (low + high) // 2

            if (nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]):
                return nums[mid]

            elif (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
                low = mid + 1
            elif (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                low = mid + 1
            else:
                high = mid - 1
        return nums[low]