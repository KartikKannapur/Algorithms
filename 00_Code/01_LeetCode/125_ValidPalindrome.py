# #Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# #For example,
# #"A man, a plan, a canal: Panama" is a palindrome.
# #"race a car" is not a palindrome.
# #Your runtime beats 87.79 % of python submissions.

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import string

        updated_str = "".join(ch.lower() for ch in s if ch.isalnum())
        return updated_str == updated_str[::-1]