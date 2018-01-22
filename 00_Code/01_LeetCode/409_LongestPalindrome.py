"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

Your runtime beats 42.93 % of python submissions
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter

        d = Counter(s)

        arr_odd = []
        arr_even = []
        for key, value in d.items():
            if (value % 2 != 0):
                arr_odd.append(value)
            elif (value % 2 == 0):
                arr_even.append(value)

        if arr_odd:
            max_value = max(arr_odd)
            arr_odd.remove(max_value)
            arr_odd = [i for i in arr_odd if i > 1]

            return max_value + sum(arr_even) + (sum(arr_odd) - len(arr_odd))
        else:
            return sum(arr_even)