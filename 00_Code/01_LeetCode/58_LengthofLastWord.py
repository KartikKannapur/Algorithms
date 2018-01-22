"""
Given a string s consists of upper/lower-case alphabets and
empty space characters ' ', return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space
characters only.
Your runtime beats 75.33 % of python submissions.
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        Method 1
        Your runtime beats 75.33 % of python submissions.
        """
        return len(s.rstrip(' ').split(' ')[-1])