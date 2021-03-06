"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Your runtime beats 88.70 % of python submissions
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        Your runtime beats 99.54 % of python submissions.
        """
        return " ".join(s.split()[::-1])