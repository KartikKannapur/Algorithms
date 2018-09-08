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


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Method 1:

        *IF the number must occur more than n/2 times in the array,
        then when the array is sorted, it must be present in the
        middle; irrespective of whether the element is the 
        smallest or the largest.
        * Sorting - O(nlogn)

        Your runtime beats 99.73 % of python submissions.
        """

        return sorted(nums)[len(nums) // 2]

