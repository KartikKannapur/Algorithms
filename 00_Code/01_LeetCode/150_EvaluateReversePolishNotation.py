"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

Your runtime beats 51.48 % of python submissions.
"""


class Solution(object):
    #     """
    #     Method 1: Stack
    #     eval()
    #     Your runtime beats 6.71 % of python submissions.
    #     """
    #     def evalRPN(self, tokens):
    #         """
    #         :type tokens: List[str]
    #         :rtype: int
    #         """

    #         s = []

    #         for ele in tokens:
    #             if ele in ["+", "-", "*", "/"]:
    #                 temp1 = s.pop()
    #                 temp2 = s.pop()

    #                 if ele == "/":
    #                     ele = "//"
    #                     new_temp = int(float(temp2)/float(temp1))
    #                 else:
    #                     new_temp = eval("(" + temp2 + ele + temp1 + ")")


    #                 s.append(str(new_temp))
    #             else:
    #                 s.append(ele)

    #         return (int(s[0]))

    """
    Method 2: Stack without eval()
    Create a dict with +-*/ operations

    Your runtime beats 87.57 % of python submissions.
    """

    def __init__(self):
        self.dict_ops = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(float(x) / float(y))
        }

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0

        s = []

        for ele in tokens:
            if ele in self.dict_ops:
                temp1 = s.pop()
                temp2 = s.pop()

                s.append(self.dict_ops[ele](temp2, temp1))
            else:
                s.append(int(ele))
        return s[0]


