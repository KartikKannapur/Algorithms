"""
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
"""


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        Method 1: Brute Force - Works
        Clears 74/84 test cases
        """
        #         slow_ptr = 0
        #         fast_ptr = 0
        #         counter = 0
        #         max_prod = 1

        #         for index in range(len(nums)):
        #             while max_prod < k and fast_ptr < len(nums):
        #                 max_prod *= nums[fast_ptr]
        #                 if max_prod < k:
        #                     counter += 1
        #                 fast_ptr += 1

        #             max_prod = 1
        #             slow_ptr += 1
        #             fast_ptr = slow_ptr

        #         return (counter)

        """
        Method 2 - Two Pointers
        Your runtime beats 9.09 % of python submissions.
        """
        slow_ptr = 0
        fast_ptr = 0
        max_prod = 1
        counter = 0
        n = len(nums)

        while slow_ptr < n:
            while fast_ptr < n and max_prod * nums[fast_ptr] < k:
                max_prod *= nums[fast_ptr]
                fast_ptr += 1

            counter += (fast_ptr - slow_ptr)

            max_prod = max(max_prod / nums[slow_ptr], 1)
            slow_ptr += 1
            fast_ptr = max(slow_ptr, fast_ptr)
        return counter
