"""
Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.


Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6


Note:

S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50

"""


class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """

        """
        Method 1:
        There are 3 replace operations we can perform to achieve the result
        replace(')(', ')+(') -- in order to obtain a sum operation
        replace('()', str(1)) -- in order to obtain the numerical value
        replace(')', ')*2') -- in order to obtain the multiplicative effect

        Your runtime beats 35.36 % of python3 submissions
        """

        S = S.replace(')(', ')+(').replace('()', str(1)).replace(')', ')*2')
        return eval(S)