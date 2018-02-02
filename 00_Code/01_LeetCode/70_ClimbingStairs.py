"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        Method 1:
        Your runtime beats 59.05 % of python submissions.
        """
        if n == 1: return 1
        if n == 2: return 2

        arr = [1, 2]
        for i in range(2, n):
            arr.append(arr[i - 1] + arr[i - 2])

        return arr[-1]