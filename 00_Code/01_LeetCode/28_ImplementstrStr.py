# #Implement strStr()
# #Return the index of the first occurrence of needle in haystack,
# #or -1 if needle is not part of haystack.
# #Example 1:
# #Input: haystack = "hello", needle = "ll"
# #Output: 2
# #Example 2:
# #Input: haystack = "aaaaa", needle = "bba"
# #Output: -1
# #Your runtime beats 68.53 % of python submissions

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # #Method 1
        try:
            return haystack.find(needle)
        except:
            return -1
