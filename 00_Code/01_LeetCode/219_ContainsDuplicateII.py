"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        """
        Method 1:
        * Enumerate through the array - nums
        * If the value exists in the dict, then check if the diff
        between the indices is atmost k
        * If not, then update the index
        Your runtime beats 89.17 % of python3 submissions.
        """
        d = dict()

        for index, val in enumerate(nums):
            if val in d:
                if (index - d[val]) <= k:
                    return True

                d[val] = index

            else:
                d[val] = index
        return False