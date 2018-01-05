"""
Given an array of characters, compress it in-place.
The length after compression must always be smaller
than or equal to the original array.

Every element of the array should be a character
(not int) of length 1.

After you are done modifying the input array in-place,
return the new length of the array.

Follow up:
Could you solve it using only O(1) extra space?

Your runtime beats 63.30 % of python submissions.
"""


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # #Method 1
        from collections import Counter
        arr = []
        for kv in Counter(chars).items():
            arr.append(kv[0])
            arr.append(str(kv[1]))

        return arr

        # #Method 2
        dict_chars = {}

        for var_char in chars:
            if var_char in dict_chars:
                dict_chars[var_char] += 1
            else:
                dict_chars[var_char] = 1

        chars = []
        for k,v in dict_chars.items():
            chars.append(k)
            chars.append(str(v))

        return len(chars)

        # #Method 3:
        anchor = write = 0
        for read, c in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write