"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Your runtime beats 86.09 % of python submissions.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        Method 1: Hash Table

        * Keep updating the index of each char
        at each iteration
        *NOTE:
        1. IF ptr < d[ch]: update ptr to ptr=d[ch]+1
        2. compare max_length with index-ptr+1

        Your runtime beats 97.18 % of python3 submissions.
        """
        ptr = 0
        max_length = 0
        d = {}

        for index, ch in enumerate(s):

            # #IF the elem is already present in the hash
            # #and the ptr is less behind, update the pointer
            # #and move it to the next index
            if ch in d and ptr <= d[ch]:
                ptr = d[ch] + 1
            else:
                max_length = max(max_length, index - ptr + 1)

            # #Constantly update the index
            d[ch] = index

        return max_length