"""
Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the
sorted order, not the kth distinct element.
For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Your runtime beats 74.38 % of python submissions
"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        Method 1: Python Sorted Function

        Complexity: O(nlogn) for sorting + O(k) for search

        Your runtime beats 98.38 % of python submissions.
        """
        # return sorted(nums, reverse=True)[k-1]

        """
        Method 2: Max Heap Solution
        Your runtime beats 45.70 % of python submissions.

        Complexity k*O(logn)
        """
        import heapq

        heap = [-1 * ele for ele in nums]
        heapq.heapify(heap)  # #Complexity O(n)

        res = 0
        # # Complexity k*O(logn)
        for _ in range(k):  # #Complexity O(k)
            res = heapq.heappop(heap)  # #Complexity O(logn)

        return -1 * res