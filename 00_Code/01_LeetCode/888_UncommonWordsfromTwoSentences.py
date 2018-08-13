"""
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.



Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]


Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.
"""

from collections import Counter


class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """

        """
        Method 1:

        * Find the words that occur only once in both the lists
        * Convert those unique words into a set and find the
        difference between the sets, both ways A-B & B-A
        * Combine the results

        53 / 53 test cases passed.
        Status: Accepted
        Runtime: 36 ms
        """

        set_A = set()
        set_B = set()

        # #Find the words that occur only once in both the lists
        counter_A = Counter(A.split())
        counter_B = Counter(B.split())

        # #Convert those unique words into a sets
        for k, v in counter_A.items():
            if v == 1 and k not in counter_B.keys():
                set_A.add(k)

        for k, v in counter_B.items():
            if v == 1 and k not in counter_A.keys():
                set_B.add(k)

        # #Combine the sets to form the result
        return list(set_A - set_B) + list(set_B - set_A)