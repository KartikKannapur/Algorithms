"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        """
        Method 1: 
        Your runtime beats 96.59 % of python submissions.
        """
        res = [[]]
        for n in nums:
            res += [res[ele] + [n] for ele in range(len(res))]
        return res


