"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
"""

from bisect import insort


class Solution:
    def findMedian(self, arr):
        """
        Custom Function written to find the median
        """
        if len(arr) % 2:
            return float(sorted(arr)[len(arr) // 2])
        else:
            temp = sorted(arr)
            return (temp[len(arr) // 2] + temp[len(arr) // 2 - 1]) / 2.0

    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        """
        Method 1: O(nk)
        Time Limit Exceeded - 30 / 42 test cases passed. 

        """

        #         if k > len(nums) or not nums:
        #             return []

        #         return [self.findMedian(nums[i:i+k]) for i in range(0, len(nums)-k+1)]


        """
        Method 2:

        Your runtime beats 1.21 % of python3 submissions :P
        """
        if k > len(nums) or not nums:
            return []

        res = []
        window = sorted(nums[:k])
        res.append(self.findMedian(window))

        for index in range(k, len(nums)):
            # #Remove the first element
            window.remove(nums[index - k])
            insort(window, nums[index])

            res.append(self.findMedian(window))

        return res
