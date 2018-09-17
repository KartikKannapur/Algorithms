"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.

 Your runtime beats 69.65 % of python submissions
"""


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        """
        Method 1

        Your runtime beats 100.00 % of python submissions.
        """
        set_1 = set("qwertyuiop")
        set_2 = set("asdfghjkl")
        set_3 = set("zxcvbnm")

        res = []
        for ele in words:
            count1 = 0
            count2 = 0
            count3 = 0

            ele_low = ele.lower()
            for char in ele_low:
                if char in set_1:
                    count1 += 1
                elif char in set_2:
                    count2 += 1
                else:
                    count3 += 1

            if (count1 == len(ele)) or (count2 == len(ele)) or (count3 == len(ele)):
                res.append(ele)

        return res

