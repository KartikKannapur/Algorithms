"""
Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting number is a power of 2.



Example 1:

Input: 1
Output: true
Example 2:

Input: 10
Output: false
Example 3:

Input: 16
Output: true
Example 4:

Input: 24
Output: false
Example 5:

Input: 46
Output: true

"""


class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """

        """
        Algorithm

        * Find the number of digits in N
        * Generete numbers that are powers of 2, such that
        the number of digits in each of those numbers is 
        less than or equal to the number of digits in N
        * For each number in the above step, store the digits
        in the sorted order - set()
        * Sort the input digits as a string and check if it
        occurs in the set

        Improvement:
        * Rather than using extra space, compare with
        sorted value of N at each iteration
        * Rather than computing the length of the str
        and using the while loop to compare each time,
        the str computation can be saved by using a
        for loop: 1 to 2^30 i.e. 2^0 -> 2^30

        Time Complexity: ??
        Space Complexity: O(k) - Space required for the set

        i = i<<1 is the same as i = i*2


        Your runtime beats 92.57 % of python submissions.
        """

        # #Sorted digits of N
        sorted_str_N = sorted(str(N))

        # #Generate powers of 2
        for i in range(0, 30):
            if sorted(str(2 ** i)) == sorted_str_N:
                return True

        return False
