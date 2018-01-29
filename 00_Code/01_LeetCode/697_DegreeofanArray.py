"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Method 1: Using a Hash
        Hash Map Schema - {element: [count, [first_occur_index, last_occur_index]]}
        Your runtime beats 64.74 % of python submissions.
        """
        if len(nums) == 1:
            return 1

        d = {}
        max_counts = 0
        for i, j in enumerate(nums):
            if j in d:
                d[j][0] += 1
                d[j][1][1] = i

                if d[j][0] > max_counts:
                    max_counts = d[j][0]
            else:
                d[j] = [1, [i, i]]
                if max_counts == 0:
                    max_counts = 1

        arr = []
        for key, value in d.items():
            if value[0] == max_counts:
                arr.append(value[1][1] - value[1][0] + 1)

        return min(arr)