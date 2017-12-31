# #Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
# #Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# #Your runtime beats 95.10 % of python submissions.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (3 * sum(set(nums)) - sum(nums)) / 2
