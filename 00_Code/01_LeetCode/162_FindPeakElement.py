"""
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        Method 1: Binary Search
        Your runtime beats 79.62 % of python submissions.
        """
        n = len(nums)
        if n == 0:
            return -1

        if n == 1:
            return 0

        low = 0
        high = n - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[mid + 1]:
                high = mid
            else:
                low = mid + 1

        return low