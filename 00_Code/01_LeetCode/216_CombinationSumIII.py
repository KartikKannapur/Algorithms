"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]

"""


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        """
        Method: DFS

        @params: nums, target, index, arr_current_res

        """

        def dfs(nums, target, index, arr_current, res):
            if target < 0:
                return None
            elif target == 0 and len(arr_current[1]) == k:
                res.append(arr_current[1])
                return None
            else:
                for i in range(index, len(nums)):
                    if i not in arr_current[0]:
                        arr_current_update = [arr_current[0] + [i], arr_current[1] + [nums[i]]]
                        dfs(nums, target - nums[i], i, arr_current_update, res)

        res = []
        target = n
        candidates = range(1, 10)
        dfs(candidates, target, 0, [[], []], res)

        res_res = []
        for ele in res:
            if sorted(ele) not in res_res:
                res_res.append(sorted(ele))

        return res_res