"""

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # #Method 1:
        # if (all(i.isupper() for i in word) == True) or (all(i.islower() for i in word) == True) or (word.capitalize() == word):
        #     return True
        # return False

        """
        Method 2: Brute Force Logic Based

        * isupper(), islower() and istitle() satisfies all the 
        three conditions

        Your runtime beats 76.00 % of python3 submissions.
        """
        return word.isupper() or word.islower() or word.istitle()
