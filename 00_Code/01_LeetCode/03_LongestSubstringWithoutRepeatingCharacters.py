__author__ = "Kartik Kannapur"

class Solution(object):
	
	def my_func(self, s, l):
		longest = s[0]
		# l = len(longest)

		for var_char in range(1, len(s)):
			if s[var_char] in longest:
				if len(longest) > l:
					l = len(longest)
				return(self.my_func(s[1:], l))

			else:
				longest += s[var_char]
				if len(longest) > l:
					l = len(longest)

		return(l)
	
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if len(s) < 1:
			return(0)
		
		elif len(s) == 1:
			return(1)
		
		else:
			return(self.my_func(s, 0))

soln = Solution()
print(soln.lengthOfLongestSubstring("aaaaaaaaaaaabcabcdefgh"))
		
		