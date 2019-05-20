"""
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

 

Example 1:

Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
 

Note:

1 <= S.length <= 20000
S consists only of English lowercase letters.
"""

class Solution:
    def removeDuplicates(self, S: str) -> str:
        
        """
        Method 1: Brute Force
        
        98 / 98 test cases passed.
        Status: Accepted
        Runtime: 336 ms
        Memory Usage: 13.3 MB
        """
#         arr = ["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii", "jj",
#               "kk", "ll", "mm", "nn", "oo", "pp", "qq", "rr", "ss", "tt",
#               "uu", "vv", "ww", "xx", "yy", "zz"]
        
#         S_old = ""
#         while S_old != S:
#             S_old = S
#             for ele in arr:
#                 if ele in S_old:
#                     S = S_old.replace(ele, "")
#                     # print(S, S_old)

#         return S

        """
        Method 2: Stack
        
        98 / 98 test cases passed.
        Status: Accepted
        Runtime: 72 ms
        Memory Usage: 13.5 MB
        """
#         stack = []
        
#         for letter in S:
#             if not stack:
#                 stack.append(letter)
#             elif stack and stack[-1] == letter:
#                 stack.pop()
#             else:
#                 stack.append(letter)
#             # print("Current Stack: ", stack)
                
#         return "".join(stack)
    
    
        """
        Method 3: Optimized Stack
        I guess :P

        98 / 98 test cases passed.
        Status: Accepted
        Runtime: 76 ms
        Memory Usage: 13.1 MB

        """
        stack = []
        
        for letter in S:
            if stack and stack[-1] == letter:
                stack.pop()
            else:
                stack.append(letter)
            # print("Current Stack: ", stack)
                
        return "".join(stack)
