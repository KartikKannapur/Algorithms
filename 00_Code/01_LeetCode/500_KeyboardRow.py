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
        # #Method 1 - Your runtime beats 69.65 % of python submissions.
        dict_chars = dict([(j, 1) for i,j in enumerate("qwertyuiop")])
        dict_chars.update(dict([(j, 2) for i,j in enumerate("asdfghjkl")]))
        dict_chars.update(dict([(j, 3) for i,j in enumerate("zxcvbnm")]))

        res = []

        for word in words:
            word_low = word.lower()
            if all(dict_chars[varchar] == dict_chars[word_low[0]] for varchar in word_low[1:]):
                res.append(word)


        return(res)

        # #Method 2
        set_1 = set("qwertyuiop")
        set_2 = set("asdfghjkl")
        set_3 = set("zxcvbnm")

        return [word for word in words if
                (set(word.lower()) - set_1 == set()) or (set(word.lower()) - set_2 == set()) or (
                set(word.lower()) - set_3 == set())]

