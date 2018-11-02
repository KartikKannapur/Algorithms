"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""


class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        """
        Method: Dynamic Programming

        * Initialize dp array with dp[0] = True
        and the rest of the dp array starting with
        False
        * Create two for loops so that we 
        can iterate over each substring in s
        * DP Logic:
        IF we can form a word until the end of the
        previous substring and the current substring
        is in wordDict as well

        dp[i] == True and s[i:j+1] in wordDict

        Complexity - O(n^2)
        Your runtime beats 54.91 % of python3 submissions.
        """

        dp = [True] + [False] * len(s)

        for i in range(len(s)):
            for j in range(i, len(s)):
                if (dp[i] == True) and (s[i:j + 1] in wordDict):
                    dp[j + 1] = True
            # print(dp)

        return dp[-1]

