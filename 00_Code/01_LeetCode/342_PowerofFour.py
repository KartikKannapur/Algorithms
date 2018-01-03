# #Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
# #Example:
# #Given num = 16, return true. Given num = 5, return false.

# #Your runtime beats 89.32 % of python submissions

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num > 0:
            if not (num & (num - 1)):

                count = 0
                while (num > 1):
                    num >>= 1
                    count += 1

                if count % 2 == 0:
                    return True
                else:
                    return False
            else:
                return False

        else:
            return False
