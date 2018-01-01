# #Determine whether an integer is a palindrome. Do this without extra space.

class Solution(object):
    def reverseNumber(self, number):

        arr_input = str(number)

        if arr_input[0] == "-":
            return "Hello"

        else:
            result = (int(arr_input[::-1]))
            return (result)

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x == self.reverseNumber(x):
            return True
        else:
            return False