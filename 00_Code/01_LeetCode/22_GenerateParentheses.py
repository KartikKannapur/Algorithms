"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        """
        0 = ()
        1 = (0)

        :::2:::
        00, (0)

        :::3:::
        "((0))","(00)","(0)0","0(0)","000"]
        """

        """
        My Initial Attempt

        res = ['']

        for i in range(n):
            print(i)

            temp = []
            for ele in res:
                temp.append(ele + '()')
                temp.append('(' + ele + ')')
                temp.append('()' + ele)

            res = list(set(temp))
            print(res)

        return res
        """

        """"""

        ans = []

        def backtrack(S='', left=0, right=0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)

        backtrack()
        return ans





