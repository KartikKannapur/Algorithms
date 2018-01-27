"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Method 1: Hash Table
        Initialize the hash table with {0: 0}
        When we come across the number 0, we subtract 1 from count
        When we come across the number 1, we add 1 to count

        At each stage, we check if count exists in the hash table.
        If it does then we update the length as the maximum between
        max_length and index-table[count]

        Reference:https://discuss.leetcode.com/topic/80056/python-o-n-solution-with-visual-explanation/2
        Your runtime beats 80.81 % of python submissions
        """
        count = 0
        max_length = 0
        table = {0: 0}

        for index, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else:
                count += 1

            if count in table:
                max_length = max(max_length, index - table[count])
            else:
                table[count] = index

        return max_length
