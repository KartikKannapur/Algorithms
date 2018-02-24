"""
Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:
Input: "x=x"
Output: "Infinite solutions"
Example 3:
Input: "2x=x"
Output: "x=0"
Example 4:
Input: "2x+3x-6x=x+2"
Output: "x=-1"
Example 5:
Input: "x=x+2"
Output: "No solution"
"""


class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """

        """
        Method 1: Brute Force
        Your runtime beats 45.06 % of python submissions.
        """

        def eval_expression(val):
            val = val.replace("+", " +").replace("-", " -").split(" ")

            x_str = ""
            x_val = 0
            for ele in val:
                if ele == "":
                    pass
                elif "x" in ele:
                    x_str += ele
                else:
                    x_val += int(ele)

            res = 0
            for ele in x_str.replace("-", "+-").split("+"):
                if ele == "":
                    pass
                elif ele == "x":
                    res += 1
                elif ele == "-x":
                    res -= 1
                else:
                    res += int(ele.split("x")[0])

            return [res, x_val]

        a_x, a_val = eval_expression(equation.split("=")[0])
        b_x, b_val = eval_expression(equation.split("=")[1])

        res = ((a_x - b_x), (a_val - b_val))

        if res[0] == res[1] == 0:
            return "Infinite solutions"

        if (a_x - b_x) == 0:
            return "No solution"

        return ("x=" + str(-1 * (a_val - b_val) / (a_x - b_x)))
