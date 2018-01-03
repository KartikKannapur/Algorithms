# #Given a string, you need to reverse the order of characters
# #in each word within a sentence while still preserving whitespace
# #and initial word order.
# #Example 1:
# #Input: "Let's take LeetCode contest"
# #Output: "s'teL ekat edoCteeL tsetnoc"
# #Note: In the string, each word is separated by single space and
# #there will not be any extra space in the string.
# #Your runtime beats 91.64 % of python submissions.

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # #Method 1
        return " ".join([var_word[::-1] for var_word in s.split(" ")])

        # #Method 2
        return ' '.join(s.split()[::-1])[::-1]