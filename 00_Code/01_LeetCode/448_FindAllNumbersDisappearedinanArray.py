"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in
this array.

Could you do it without extra space and in O(n) runtime? You may
assume the returned list does not count as extra space.

Your runtime beats 86.88 % of python submissions.
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # #Method 1
        return list(set(range(1,len(nums)+1)) - set(nums))
