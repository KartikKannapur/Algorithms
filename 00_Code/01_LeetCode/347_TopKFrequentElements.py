"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # from collections import Counter
        # return [ele[0] for ele in Counter(nums).most_common(k)]

        return [item[0] for item in collections.Counter(nums).most_common(k)]