"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Your runtime beats 39.35 % of python submissions
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #Method 1: Using Stack
        stack = []

        for p in s:
            if p == "{":
                stack.append(p)
            if p == "(":
                stack.append(p)
            if p == "[":
                stack.append(p)

            try:
                if p == "}":
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
                if p == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                if p == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
            except:
                return False
        if len(stack) > 0: return False
        else: return True

        # #Method 2: Optimized Stack Code
        stack = []
        dict = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

        # #Method 3: String Manipulation - O(N^2) - Worst Time Complexity
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()","").replace("{}","").replace("[]","")
        return len(s) == 0
