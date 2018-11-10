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


class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        """
        Method 1: 

        * Start with an empty [[]] array    
        * FOR each element in nums:
        Add the element to the array:
        * INNER FOR loop, add [element + each element in res]
        and update res

        Your runtime beats 99.88 % of python3 submissions.
        """

        res = [[]]

        for n in nums:
            res += [ele + [n] for ele in res]
        return res

