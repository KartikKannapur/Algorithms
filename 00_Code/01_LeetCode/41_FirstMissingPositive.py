"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.

"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        Method: Brute Force

        * Sort the array
        * Traverse through the array until we find the 
        first positive number
        * Let res= 1
        * When we encounter a positive number == res,
        increment res to the next number

        Your runtime beats 100.00 % of python submissions.
        """

        nums.sort()
        res = 1

        for ele in nums:
            if ele == res:
                res += 1

        return res