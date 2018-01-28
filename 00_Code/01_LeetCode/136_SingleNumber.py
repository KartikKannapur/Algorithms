"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Method 1
        Create a hash table - dictionary and keep a track of the number
        of occurrances of each element. The element that occurs only once
        will be the 'single one'

        Method 2
        Create an array O(n) space. Append the element if its not in the 
        array; delete the element from the array if you encounter it again.
        The remaining element will be the 'single one'
        """

        """
        Method 3
        Your runtime beats 91.85 % of python submissions
        """
        return 2 * sum(set(nums)) - sum(nums)