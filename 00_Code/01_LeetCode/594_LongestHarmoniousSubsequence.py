"""
We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.
"""


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Method 1:
        We could also emplot a sorting based approach, but that would be
        O(nlogn)
        """

        #         """
        #         Method 2:
        #         Essentially, we just need the total number of counts of (n)th and (n+1)th
        #         numbers; and we need to find the maximum such number
        #         Complexity - O(n)
        #         Your runtime beats 56.77 % of python submissions
        #         """
        #         from collections import Counter
        #         dict_counts = Counter(nums)

        #         max_length = 0
        #         for ele in dict_counts:
        #             if (ele+1) in dict_counts:
        #                 max_length = max(max_length, (dict_counts[ele] + dict_counts[ele+1]))

        #         return max_length

        """
        Method 3:
        Same as Method 2, but without the built-in function
        Your runtime beats 99.74 % of python submissions.
        It's surprising that the manually implemented dict_counts
        works much faster than the Counter module.
        """
        dict_counts = {}
        for ele in nums:
            if ele not in dict_counts:
                dict_counts[ele] = 1
            else:
                dict_counts[ele] += 1

        max_length = 0
        for ele in dict_counts:
            if (ele + 1) in dict_counts:
                max_length = max(max_length, (dict_counts[ele] + dict_counts[ele + 1]))

        return max_length

