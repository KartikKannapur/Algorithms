"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

Your runtime beats 34.18 % of python submissions.
"""


class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        """
        Method 1: Brute Force

        * Maintain a dict with the character and count
        * Sort the dictionary based on decreasing order of value
        * Append the character to the res string, as many times
        as the value

        Your runtime beats 51.80 % of python3 submissions.
        """

        # #Maintain a dict with the character and count
        d = {}
        for char in s:
            if char in d.keys():
                d[char] += 1
            else:
                d[char] = 1

        # #Sort the dictionary based on decreasing order of value
        arr_res = sorted(d.items(), key=lambda ele: ele[1], reverse=True)

        # #Append the character to the res string, as many times as the value
        res = ""
        for char, count in arr_res:
            res += char * count

        return res