"""

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution:
    def subsetsWithDup(self, nums):
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

        Your runtime beats 39.19 % of python3 submissions.
        """

        res = [[]]

        for n in nums:
            res += [ele + [n] for ele in res if ele + [n] not in res]

        res_res = []
        for eelee in [sorted(ele) for ele in res]:
            if eelee not in res_res:
                res_res.append(eelee)

        return res_res
