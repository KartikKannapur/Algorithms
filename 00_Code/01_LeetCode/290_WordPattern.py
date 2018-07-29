"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

"""


class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        """
        Method 1 - Hash Map
        This question is the same as 205. Isomorphic Strings
        I have used the same logic, but I've substituted
        s=pattern
        t=str.split(" ")

        Your runtime beats 72.25 % of python3 submissions.
        """
        s = pattern
        t = str.split(" ")

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
