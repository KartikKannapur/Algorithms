"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        Method 1

        * We need to find ALL elements that occur more than n//3 times
        * Loop over all the elements and check their counts

        Your runtime beats 99.57 % of python3 submissions
        """
        return [x for x in set(nums) if nums.count(x) > len(nums) // 3]