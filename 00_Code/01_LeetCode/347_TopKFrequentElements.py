"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Your runtime beats 52.16 % of python submissions.
"""


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        """
        Method 1: Counter Based Method

        Your runtime beats 100.00 % of python3 submissions
        """
        # return [item[0] for item in collections.Counter(nums).most_common(k)]

        """
        Method 2: Using a hash map without Counter

        * Create a hash map with {element : count}
        * Sort the hash map in reverse order and select first k elements

        Your runtime beats 68.42 % of python3 submissions.
        """
        d = {}
        for ele in nums:
            if ele in d:
                d[ele] += 1
            else:
                d[ele] = 1
        return [ele[0] for ele in sorted(d.items(), key=lambda x: x[1], reverse=True)][:k]
