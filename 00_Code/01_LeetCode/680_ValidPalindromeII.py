# #Given a non-empty string s, you may delete at most one character.
# #Judge whether you can make it a palindrome.
# #Example 1:
# #Input: "aba"
# #Output: True
# #Example 2:
# #Input: "abca"
# #Output: True
# #Explanation: You could delete the character 'c'.

# #Your runtime beats 69.28 % of python submissions.

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counter = 0
        while counter < len(s) / 2 and s[counter] == s[-(counter + 1)]:
            counter += 1
        s = s[counter:len(s) - counter]
        return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]
