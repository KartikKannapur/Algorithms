"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        """
        Method 1: Using the count module in Python
        254 / 254 test cases passed.
        Status: Accepted
        Runtime: 38 ms
        """
        counter = 0

        for ele in set(J):
            counter += S.count(ele)

        return counter

        """
        Method 2: Using a hash table
        254 / 254 test cases passed.
        Status: Accepted
        Runtime: 38 ms
        """
        dict_stones = {}
        for ele in S:
            if ele not in dict_stones:
                dict_stones[ele] = 1
            else:
                dict_stones[ele] += 1

        res = 0
        for ele in set(J):
            if ele in dict_stones:
                res += dict_stones[ele]
        return res

        """
        Method 3: One-liner
        Method 2: Using a hash table
        254 / 254 test cases passed.
        Status: Accepted
        Runtime: 37 ms
        """
        return sum([S.count(ele) for ele in set(J)])