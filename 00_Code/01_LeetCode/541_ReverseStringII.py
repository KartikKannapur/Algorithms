# #Given a string and an integer k, you need to reverse the first
# #k characters for every 2k characters counting from the start
# #of the string. If there are less than k characters left,
# #reverse all of them. If there are less than 2k but greater than
# # or equal to k characters, then reverse the first k characters
# #and left the other as original.

# #Example:
# #Input: s = "abcdefg", k = 2
# #Output: "bacdfeg"
# #Your runtime beats 82.02 % of python submissions.


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Method 1
        new_string = ""

        i = 0
        while i < len(s):
            new_string += s[i:i + k][::-1] + s[i + k:i + (2 * k)]
            i += (2 * k)

        return new_string

        # #Method 2
        return s[:k][::-1] + s[k:2 * k] + self.reverseStr(s[2 * k:], k) if s else ""
