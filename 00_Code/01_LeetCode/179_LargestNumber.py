"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        """
        Method 1:
        179 / 221 test cases passed.

        Convert each element in the array into a string
        Sort and Join the array
        """
        # return "".join(sorted(list(map(str, nums)), reverse=True))

        """
        Method 2:
        Your runtime beats 99.76 % of python submissions.
        """
        return str(int(''.join(sorted(map(str, nums), key=lambda s: s * 9, reverse=True))))
