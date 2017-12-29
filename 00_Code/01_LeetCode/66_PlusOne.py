# #Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
# #You may assume the integer do not contain any leading zero, except the number 0 itself.
# #The digits are stored such that the most significant digit is at the head of the list.
# #Your runtime beats 95.60 % of python submissions.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # #Method 1
        return list(map(int, list(str(int("".join(list(map(str, digits)))) + 1))))

        # #Method 2
        n = len(digits)

        digits[n - 1] += 1
        for d in range(0, n):
            if digits[n - d - 1] % 10 == 0:
                digits[n - d - 2] += 1
                digits[n - d - 1] = 0

        return (digits)