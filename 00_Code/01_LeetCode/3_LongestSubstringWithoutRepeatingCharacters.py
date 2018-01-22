"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Your runtime beats 86.09 % of python submissions.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        next_ptr = 0
        max_length = 0
        d = {}

        for i in range(len(s)):
            if s[i] in d and next_ptr <= d[s[i]]:
                next_ptr = d[s[i]] + 1
            else:
                max_length = max(max_length, i - next_ptr + 1)

            d[s[i]] = i

        return max_length
