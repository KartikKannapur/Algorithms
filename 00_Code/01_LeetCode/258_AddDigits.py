# #Given a non-negative integer num, repeatedly add all its
# #digits until the result has only one digit.
# #For example:
# #Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2.
# #Since 2 has only one digit, return it.
# #Your runtime beats 88.85 % of python submissions.

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # #Method 1:
        def listsum(numList):
            theSum = 0
            for i in numList:
                theSum = theSum + i
            return theSum

        while len(str(num)) > 1:
            num = listsum(list(map(int, list(str(num)))))

        return num

        # #Method 2
        if num == 0:
            return 0
        else:
            return (num - 1) % 9 + 1
