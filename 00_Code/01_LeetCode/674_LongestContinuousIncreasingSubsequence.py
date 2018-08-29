"""
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1.
Note: Length of the array will not exceed 10,000.
"""


class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        Method 1:

        * Every (continuous) increasing subsequence is disjoint.

        * Keep an index pointer, a main counter and a temp counter
        for each subarray
        * As long as nums[index-1] < nums[index], keep incrementing
        the counter

        Your runtime beats 65.05 % of python3 submissions
        """

        # #Handle boundary conditions
        if not nums:
            return 0

        # #Initialize variables
        index = 1
        count = -1
        tempCount = 1

        while index < len(nums):
            if nums[index - 1] < nums[index]:
                tempCount += 1
            else:
                count = max(count, tempCount)
                tempCount = 1
            index += 1

        count = max(count, tempCount)
        return count