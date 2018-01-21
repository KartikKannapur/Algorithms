"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Your runtime beats 70.47 % of python submissions.~
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        Method 1: Stack Code
        Your runtime beats 39.35 % of python submissions.
        """
        #         stack = []
        #         dict = {"]":"[", "}":"{", ")":"("}

        #         for char in s:
        #             if char in dict.values():
        #                 stack.append(char)
        #             elif char in dict.keys():
        #                 if stack == [] or dict[char] != stack.pop():
        #                     return False
        #             else:
        #                 return False
        #         return stack == []

        """
        Method 2: Optimized Stack Code

        Create a dict with the key-value pairs being
        either pairs of a parentheses set.

        Check if the last element in the stack is the same as

        Your runtime beats 70.47 % of python submissions.
        """
        d = {"]": "[", "}": "{", ")": "("}
        stack = []

        for char in s:
            if stack and (char in d and stack[-1] == d[char]):
                stack.pop()
            else:
                stack.append(char)
        return stack == []
