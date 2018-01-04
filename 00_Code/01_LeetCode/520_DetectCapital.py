# #Given a word, you need to judge whether the usage of capitals
# #in it is right or not.
# #We define the usage of capitals in a word to be right when one
# #of the following cases holds:
# #All letters in this word are capitals, like "USA".
# #All letters in this word are not capitals, like "leetcode".
# #Only the first letter in this word is capital if it has more
# #than one letter, like "Google".
# #Otherwise, we define that this word doesn't use capitals in a right way

# #Your runtime beats 54.41 % of python submissions.

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # #Method 1:
        if (all(i.isupper() for i in word) == True) or (all(i.islower() for i in word) == True) or (
            word.capitalize() == word):
            return True
        return False

        # #Method 2:
        return word.isupper() or word.islower() or word.istitle()
