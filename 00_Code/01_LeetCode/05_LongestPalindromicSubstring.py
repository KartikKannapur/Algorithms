"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

         """
        Method: Dynamic Programming
        
        * Create a 2D dp array
        * for i in range(n):
            for j in range(i, -1, -1)
            
        * IF the indices (j-i) < 2 indicating 0 or 1
        and if the i-1, j+1 i.e top right element is True
        then dp of this element is True
        
        
        Your runtime beats 24.40 % of python3 submissions.
        """

        n = len(s)
        dp = [[False]*n for _ in range(n)]
        res = ""

        '''
        If the string s were 'babad', think this:
                            j
                        b a b a d             0 1 2 3 4
                     b  T                  0  T
                     a    T                1 <- T
                i    b  T   T          i   2  T   T
                     a    T   T            3    <-- T
                     d          T          4          so on.
        iterations go left. checks top right. Checking top right is like 
        saying if u got substring 'baab' and u check top right for 'aa'.
        '''
        for i in range(n):
            for j in range(i, -1, -1):
                # if they are equal and (the substring is length 2 or 1  or  the inner substring is also palindrom by looking up-right)
                if s[i] == s[j] and (i-j < 2 or dp[i-1][j+1]):
                    dp[i][j] = True

                # if earlier if statement were True, get longer result
                if dp[i][j] and (i-j+1)  > len(res):
                    res = s[j:i+1]
        return res