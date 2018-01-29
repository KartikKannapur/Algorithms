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
        Method 1: itertools module
        Your runtime beats 97.75 % of python submissions.
        """
        from itertools import permutations
        return list(permutations(nums))


        """
        Method 2: Recursion - Backtracking
        Your runtime beats 17.17 % of python submissions.
        """

        def permutation(lst):
            if len(lst) == 1:
                return [lst]

            l = []
            for i in range(len(lst)):
                remLst = lst[:i] + lst[i + 1:]

                for p in permutation(remLst):
                    l.append([lst[i]] + p)
            return l

        arr = []
        for p in permutation(nums):
            arr.append(p)
        return arr

        """
        Method 3: Backtracking
        Your runtime beats 31.88 % of python submissions.
        """
        def backtrack(start, end):
            if start == end:
                ans.append(nums[:])

            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1, end)
                nums[start], nums[i] = nums[i], nums[start]

        ans = []
        backtrack(0, len(nums))
        return ans