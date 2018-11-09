"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        """
        Method: DFS

        * Solution is the same as Permutation I,
        the only addition is I am also checking
        if path is already present in res


        In order to optimize this code, we could
        use a hash map to not consider elements
        that are already traversed
        """

        def dfs(nums, path, res):
            if not nums:
                if path not in res:
                    res.append(path)

            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)

        res = []
        dfs(nums, [], res)
        return res