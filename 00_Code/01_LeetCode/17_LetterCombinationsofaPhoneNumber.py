"""
Given a digit string, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.
dict_numbers = {"2" : list("abc"), "3" : list("def"),
                "4" : list("ghi"), "5" : list("jkl"),
                "6" : list("mno"), "7" : list("pqrs"),
                "8" : list("tuv"), "9" : list("wxyz")}

"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        """
        Method 1
        Your runtime beats 58.77 % of python submissions.
        Among all the other solutions - Iterative, Backtracking; this method
        seemed to yield the best accuracy.
        """
        #         from itertools import product
        #         digits = list(digits)
        #         prod = ["".join(i) for i in product(dict_numbers[digits[0]])]

        #         for k in range(1,len(digits)):
        #             prod = ["".join(i) for i in product(prod, dict_numbers[digits[k]])]

        #         return(prod)

        """
        Method 2 - Backtracking

        Your runtime beats 100.00 % of python submissions
        """

        dict_numbers = {"2": list("abc"), "3": list("def"),
                        "4": list("ghi"), "5": list("jkl"),
                        "6": list("mno"), "7": list("pqrs"),
                        "8": list("tuv"), "9": list("wxyz")}

        if digits == "":
            return []
        """
        Standard Backtracking format
        Start with an inital value for res
        Iterate through digits and res, so as to update res
        """
        res = dict_numbers[digits[0]]
        for ele in digits[1:]:
            res = [i + j for i in res for j in dict_numbers[ele]]

        return res
