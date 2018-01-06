"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

Your runtime beats 83.76 % of python submissions.
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #Method 1
        maxval = 0
        counter = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
                if i == len(nums)-1:
                    if counter > maxval: maxval = counter
            else:
                if counter > maxval: maxval = counter
                counter = 0

        return maxval

        # #Method 2
        return len(max(str(nums)[1:-1].replace(", ", "").split("0")))
