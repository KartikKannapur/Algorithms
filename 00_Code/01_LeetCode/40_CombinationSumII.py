"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        """
        Method: DFS

        @params: nums, target, index, arr_current_res

        """

        def dfs(nums, target, index, arr_current, res):
            if target < 0:
                return None
            elif target == 0:
                res.append(arr_current[1])
                return None
            else:
                for i in range(index, len(nums)):
                    if i not in arr_current[0]:
                        arr_current_update = [arr_current[0] + [i], arr_current[1] + [nums[i]]]
                        dfs(nums, target - nums[i], i, arr_current_update, res)

        res = []
        dfs(candidates, target, 0, [[], []], res)

        res_res = []
        for ele in res:
            if sorted(ele) not in res_res:
                res_res.append(sorted(ele))

        return res_res