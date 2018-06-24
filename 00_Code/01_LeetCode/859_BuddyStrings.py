"""
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.



Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false


20 / 20 test cases passed.
Status: Accepted
Runtime: 38 ms
"""

class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """

        # #Method 1:
        # #Case 1
        if len(A) != len(B):
            return False

        # #Case 2
        counter = 0
        if len(A) == len(B):
            for i in range(len(A)):
                if A[i] != B[i]:
                    counter += 1

        if counter == 1 or counter > 2:
            return False

        # #Case 3
        elif counter == 2:
            return set(A) == set(B)

        # #Case 4
        else:
            return len(set(A)) != len(A)