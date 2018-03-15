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
        """
        Method 1: Hash Table
        Your runtime beats 88.39 % of python submissions.

        FOR each elem in the string:
        IF the elem is present in the hash and the ptr is behind: update it
        ELSE update the max length

        Constantly keep updating th index
        """
        ptr = 0
        max_length = 0
        d = {}

        for index, ch in enumerate(s):

            # #IF the elem is already present in the hash
            # #increment the pointer by 1
            if ch in d and ptr <= d[ch]:
                ptr = d[ch] + 1
            else:
                max_length = max(max_length, index - ptr + 1)

            # #Constantly update the index
            d[ch] = index

        return max_length