"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

Your runtime beats 51.48 % of python submissions.
"""


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        """
        Method 1: Stack
        eval()
        Your runtime beats 6.71 % of python submissions.
        """
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

        Your runtime beats 51.48 % of python submissions.
        """
        dict_ops = {
            '+': lambda x, y: int(float(x) + float(y)),
            '-': lambda x, y: int(float(x) - float(y)),
            '*': lambda x, y: int(float(x) * float(y)),
            '/': lambda x, y: int(float(x) / float(y))
        }

        s = []

        for ele in tokens:
            if ele in ['+', '-', '*', '/']:
                temp1 = s.pop()
                temp2 = s.pop()

                s.append(dict_ops[ele](temp2, temp1))
            else:
                s.append(int(ele))
        return s[0]





