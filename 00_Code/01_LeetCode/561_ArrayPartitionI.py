"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].
"""


class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        Method 1:
        * Sort the array
        * Create consecutive pairs implying that the digits in 
        each pair would not be very far away from each other.
        This would help us in maximizing the sum of the 
        minimums.

        Your runtime beats 32.28 % of python3 submissions
        """

        #         nums.sort()

        #         res = 0
        #         for index in range(0, len(nums), 2):
        #             # print(index, index+1, nums[index], nums[index+1])
        #             res += min(nums[index], nums[index+1])

        #         return res

        """
        Method 2:
        Same logic

        * When we sort the array and group the pairs,
         the minimum elements will always be alternate.
         Therefore, it would suffice to sum[nums[::2]]

        Your runtime beats 90.41 % of python3 submissions.
        """

        nums.sort()

        return sum(nums[::2])