"""

Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

"""


class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Method 1: Brute Force
        Algorithm works well, but TLE
        """
        counter = 0
        while len(set(nums)) != 1:
            max_index = nums.index(max(nums))

            for i in range(len(nums)):
                if i != max_index:
                    nums[i] += 1

            counter += 1

        return (counter)

        """
        Method 2: Math
        sum + m * (n - 1) = x * n
        x = minNum + m
        sum - minNum * n = m

        Your runtime beats 84.40 % of python submissions.
        """

        return sum(nums) - (min(nums) * len(nums))