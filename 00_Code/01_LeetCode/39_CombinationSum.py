"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        """
        Method: DFS

        @params: nums, target, index, arr_current_res

        Your runtime beats 66.17 % of python submissions.
        """

        def dfs(nums, target, index, arr_current, res):
            if target < 0:
                return None
            elif target == 0:
                res.append(arr_current)
                return None
            else:
                for i in range(index, len(nums)):
                    dfs(nums, target - nums[i], i, arr_current + [nums[i]], res)

        res = []
        dfs(candidates, target, 0, [], res)
        return res