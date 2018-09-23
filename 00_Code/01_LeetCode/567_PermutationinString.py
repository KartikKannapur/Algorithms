"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""


class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        """
        Method 1: Sliding window over the array


        Similar to Q438?

        * Create a sliding window of size = len(s1)
        and traverse over the array s2
        * At each window, check if the window and s1
        are anagrams of each other or not i.e some permutation

        Completed 72/102 cases. TLE. This should be okay. I'll take it
        """
                res_index = []

                for index in range(len(s2)+1-len(s1)):
                    # print(s2[index:index+len(s1)])
                    if sorted(s2[index:index+len(s1)]) == sorted(s1):
                        return True

                return False

        # #Solution from the Discussion Forum
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]

        target = [0] * 26
        for x in A:
            target[x] += 1

        window = [0] * 26
        for i, x in enumerate(B):
            window[x] += 1
            if i >= len(A):
                window[B[i - len(A)]] -= 1
            if window == target:
                return True
        return False
