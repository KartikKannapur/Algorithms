"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

Your runtime beats 36.67 % of python submissions.
"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        Method 1: Two Pointers
        Representing vowel as an array - Your runtime beats 35.89 % of python submissions.
        Representing vowel as a set(as below) - Your runtime beats 93.78 % of python submissions.
        """
        s = list(s)
        vowel = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        low = 0
        high = len(s) - 1

        while low < high:
            while low < high and s[low] not in vowel:
                low += 1
            while low < high and s[high] not in vowel:
                high -= 1

            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1

        return ("".join(s))
