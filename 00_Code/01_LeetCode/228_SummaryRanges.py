"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
"""


class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        """
        Method: Array

        Your runtime beats 100.00 % of python3 submissions.
        """
        # #Boundary Conditions
        if not nums:
            return []

        # #Initialization
        res = []
        low = nums[0]
        high = nums[0]

        for i in range(1, len(nums)):
            high = nums[i]
            if nums[i] - 1 != nums[i - 1]:
                high = nums[i - 1]
                res.append([low, high])

                low = nums[i]
                high = nums[i]

        # #Update the last element
        res.append([low, high])

        res_res = []
        for ele in res:
            if ele[0] == ele[1]:
                res_res.append(str(ele[0]))
            else:
                res_res.append(str(ele[0]) + "->" + str(ele[1]))

        return res_res