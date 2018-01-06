"""
Given two strings representing two complex numbers.

You need to return a string representing their multiplication.
Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you
need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you
need convert it to the form of 0+-2i.
Note:

The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the
integer a and b will both belong to the range of [-100, 100].
And the output should be also in this form.

Your runtime beats 49.77 % of python submissions
"""

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # #Method 1
        r1, im1 = a.split("+")
        r2, im2 = b.split("+")

        r1, r2 = int(r1), int(r2)
        im1, im2 = int(im1[:-1]), int(im2[:-1])

        return str((r1*r2) - (im1*im2)) + str("+") + str((r1*im2) + (r2*im1)) + "i"
