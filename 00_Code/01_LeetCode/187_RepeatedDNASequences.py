 """
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
"""

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        """
        Method 1: Brute Force + Dictionary
        Your runtime beats 46.08 % of python submissions.
        """
        if not s or len(s) < 10:
            return []

        d = {}
        for i in range(len(s) - 9):
            d[s[i:i + 10]] = d.get(s[i:i + 10], 0) + 1
        return [res for res in d.keys() if d[res] > 1]