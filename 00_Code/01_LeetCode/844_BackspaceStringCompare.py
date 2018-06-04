"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.



Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
"""


class Solution(object):
    #     """
    #     Method 1:

    #     Create a new method to generate a clean string(without #)
    #     IF a # is present in the string, remove the # and the previous character
    #     via string slicing
    #     Repeat this process until no # is present in the string

    #     104 / 104 test cases passed.
    #     Status: Accepted
    #     Runtime: 37 ms
    #     """
    #     def generateCleanStr(self, word):
    #         while '#' in word:
    #             index = word.index('#')
    #             if index != 0:
    #                 word = word[:index-1] + word[index+1:]
    #             else:
    #                 word = word[index+1:]

    #         return word

    #     def backspaceCompare(self, S, T):
    #         """
    #         :type S: str
    #         :type T: str
    #         :rtype: bool
    #         """
    #         return self.generateCleanStr(S) == self.generateCleanStr(T)

    """
    Method 2:
    104 / 104 test cases passed.
    Status: Accepted
    Runtime: 33 ms
    """

    def generateCleanStr(self, word):
        new_word = []
        for c in word:
            if c != '#':
                new_word.append(c)
            elif new_word:
                new_word.pop()
        return "".join(new_word)

    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.generateCleanStr(S) == self.generateCleanStr(T)
