"""
Given an arbitrary ransom note string and another string
containing letters from all the magazines, write a function
that will return true if the ransom note can be constructed
from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in
your ransom note.

Note:
You may assume that both strings contain only lowercase
letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

Your runtime beats 94.83 % of python submissions.
"""


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # #Method 1:
        from collections import Counter
        ransom_counter = Counter(list(ransomNote))
        magazine_counter = Counter(list(magazine))

        for k,v in ransom_counter.items():
            try:
                if v > magazine_counter[k]:
                    return False
            except:
                return False
        return True

        # #Method 2:
        dict_ransom = {}
        dict_magazine = {}

        for var_letter in list(ransomNote):
            if var_letter in dict_ransom:
                dict_ransom[var_letter] += 1
            else:
                dict_ransom[var_letter] = 1

        for var_letter in list(magazine):
            if var_letter in dict_magazine:
                dict_magazine[var_letter] += 1
            else:
                dict_magazine[var_letter] = 1

        for k,v in dict_ransom.items():
            try:
                if v > dict_magazine[k]:
                    return False
            except:
                return False
        return True

        # #Method 3:
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True
