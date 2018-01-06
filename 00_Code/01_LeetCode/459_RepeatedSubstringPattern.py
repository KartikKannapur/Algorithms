"""
Given a non-empty string check if it can be constructed
by taking a substring of it and appending multiple copies
of the substring together. You may assume the given string
consists of lowercase English letters only and its length
will not exceed 10000.
Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the
substring "abcabc" twice.)

Your runtime beats 76.37 % of python submissions.
"""


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # #Method 1:
        i = 1
        while i != len(s):
            if s[:i]*(len(s)//len(s[:i])) == s:
                return True
            i += 1
        return False

        # #Method 2:
        i = len(s)-1
        while i > 0:
            if s[:i]*(len(s)//len(s[:i])) == s:
                return True
            i -= 1
        return False

        # #Method 3
        return any(s[:i] * (len(s) / i) == s for i in range(1, len(s)) if len(s) % i == 0)

        # #Method 4
        if not s:
            return False

        ss = (s + s)[1:-1]
        return ss.find(s) != -1


