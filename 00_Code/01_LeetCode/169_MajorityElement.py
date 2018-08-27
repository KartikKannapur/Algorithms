"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        Method 1 - Using a Counter/Dictionary
        Your runtime beats 61.71 % of python3 submissions
        """
        # return [x for x in set(nums) if nums.count(x) > len(nums) // 2][0]


        """
        Method 2

        * Sort the array
        * The element in the middle should have occurred atleast n//2 times

        Your runtime beats 61.71 % of python3 submissions
        """
        return sorted(nums)[(len(nums) // 2)]
