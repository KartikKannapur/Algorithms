"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """
        Method 1 - Hash Map
        - Basic check: If the two strings are of equal length
        - Iteratively add elements and check the hash map
        - O(n) operation

        Your runtime beats 99.27 % of python submissions.
        """
        if len(s) != len(t):
            return False

        d = {}

        for index, letter in enumerate(s):
            if letter in d:
                if d[letter] != t[index]:
                    return False
            elif t[index] in d.values():
                return False
            else:
                d[letter] = t[index]

        return True