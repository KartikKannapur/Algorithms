"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Your runtime beats 70.47 % of python submissions.~
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        """
        Method 1: Stack Code
        Your runtime beats 39.35 % of python submissions.
        """

        """
        Method 2: Optimized Stack Code

        Create a hash map with the key-value pairs being
        either pairs of a parentheses set in reverse order.

        Check if the last element in the stack is the same as
        the current element in the hash map

        Your runtime beats 98.91 % of python3 submissions.
        """
        d = {"]": "[", "}": "{", ")": "("}
        stack = []

        for char in s:
            if stack and (char in d) and (stack[-1] == d[char]):
                stack.pop()
            else:
                stack.append(char)
        return not stack  # #If stack is empty: return True; else return False
