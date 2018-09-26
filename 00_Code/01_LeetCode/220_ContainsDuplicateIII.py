"""
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
"""


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        """
        Method 1: Sliding Window in Array

        i: 0 to len(nums)
        j: i+1 to i+k+1

        TLE - But I'll take it
        """

        #         for i in range(len(nums)):
        #             for j in range(i+1, i+k+1):
        #                 if j<len(nums) and abs(nums[i]-nums[j]) <= t:
        #                     return True
        #         return False

        # #Discussion Forum
        ind = sorted(range(len(nums)), key=lambda x: nums[x])
        for i in range(len(nums) - 1):
            j = i + 1
            while j < len(nums) and nums[ind[j]] - nums[ind[i]] <= t:
                if abs(ind[i] - ind[j]) <= k:
                    return True
                j += 1
        return False