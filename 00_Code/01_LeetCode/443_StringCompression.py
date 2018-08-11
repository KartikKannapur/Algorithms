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


class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        """
        Method 1: collection.Counter() or Hash Map() 
        """

        """
        Method 2:

        * IF a single element is present in the array, return 1
        * Initialize current_ptr=0, current_letter=chars[0]
        and a counter to count the number of consecutive letters
        * Enumerate through the array
        IF the chars is same increment the counter. 
        IF the chars is different, update the letter and counter
        values in the array and move on
        Your runtime beats 99.71 % of python3 submissions
        """

        # #Handling edge cases
        # #IF a single element is present in the array, return 1
        if len(chars) == 1:
            return 1

        # #Initialization
        current_ptr = 0
        current_letter = chars[0]
        counter = 0

        # #Enumerate through the array
        for index, letter in enumerate(chars):
            if letter == current_letter:
                counter += 1
            else:
                chars[current_ptr] = current_letter
                current_ptr += 1

                # #Logic to handle cases specific to this code
                if counter > 1:
                    for ele in list(str(counter)):
                        chars[current_ptr] = str(ele)
                        current_ptr += 1

                counter = 1
                current_letter = letter

        # #Code to handle the last character
        chars[current_ptr] = current_letter
        # #Logic to handle cases specific to this code
        if counter > 1:
            for ele in list(str(counter)):
                current_ptr += 1
                chars[current_ptr] = str(ele)

        chars[:] = chars[:current_ptr + 1]