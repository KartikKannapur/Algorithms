"""
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].

"""


class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        """
        Method 1: Brute Force

        * Create a moving window across the input array
        * For each window calculate the average value
        and find the maximum.

        Time Limit Exceeded
        67 / 123 test cases passed.
        """
        #         res_avg = -1

        #         for i in range(0, len(nums)-k+1):
        #             avg = sum(nums[i:i+k])/k
        #             res_avg = max(res_avg, avg)

        #         return res_avg

        """
        Method 2:

        * Similar logic as method 1, but ranther than
        subsetting the array each time, we remove the
        first element and append the last to create
        a moving window.

        Your runtime beats 66.97 % of python3 submissions.
        """

        window_sum = sum(nums[:k])
        res_avg = window_sum / k

        for i in range(k, len(nums)):
            window_sum = window_sum + nums[i] - nums[i - k]
            res_avg = max(res_avg, window_sum / k)

        return res_avg