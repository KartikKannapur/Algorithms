"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
Your runtime beats 47.05 % of python submissions.
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        """
        Algorithm:

        * Count the number of occurrences of each
        character in both s and t and compare if they
        are equal

        Your runtime beats 35.24 % of python submissions.
        """
        return sorted(s) == sorted(t)
