"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        """
        Method 1: Python Built-in function
        """
        # try:
        #     return haystack.find(needle)
        # except:
        #     return -1

        """
        Method 2: Sliding Window
        Your runtime beats 67.60 % of python submissions.
        """
        k = len(needle)
        for index in range(len(haystack) - k + 1):
            if haystack[index:index + k] == needle:
                return index
        return -1