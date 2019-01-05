"""
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.



Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
"""


class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """

        """
        Method: Two Pointers

        Your runtime beats 98.74 % of python3 submissions.
        """

        S = list(S)
        low = 0
        high = len(S) - 1

        while low < high:
            if not S[low].isalpha():
                low += 1
            elif not S[high].isalpha():
                high -= 1

            else:
                S[low], S[high] = S[high], S[low]
                low += 1
                high -= 1

        return "".join(S)