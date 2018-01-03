# #The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# #Given two integers x and y, calculate the Hamming distance.
# #Your runtime beats 84.64 % of python3 submissions

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # #Method 1
        num_1 = bin(x)[2:].zfill(31)
        num_2 = bin(y)[2:].zfill(31)

        var_counter = 0
        for i in range(0, 31):
            if num_1[i] != num_2[i]:
                var_counter += 1
        return (var_counter)

        # #Method 2:
        return bin(x^y).count('1')