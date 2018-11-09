"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        """
        Method: DFS

        * At each iteration we update the parameters
        in the dfs method.
        * dfs(nums, path, res)
        * We update nums by removing the current element
        * We update path by adding the current element
        * When the nums array is empty, we update res   

        Your runtime beats 99.81 % of python submissions.
        """

        def dfs(nums, path, res):
            if not nums:
                res.append(path)

            for i in range(len(nums)):
                # #Update nums and path
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)

        res = []
        dfs(nums, [], res)
        return res
