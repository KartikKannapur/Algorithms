"""
Given two non-negative integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.

Return a list of all powerful integers that have value less than or equal to bound.

You may return the answer in any order.  In your answer, each value should occur at most once.



Example 1:

Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation:
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2
Example 2:

Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14]


Note:

1 <= x <= 100
1 <= y <= 100
0 <= bound <= 10^6
"""


class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        """
        Method 1: Brute Force

        * We need all combinations of the values
        of x**i and y**j in order to check if they
        lie within the given range. Therefore, in
        order to do this, we first create two 
        arrays with all the values.
        * Once we have generate these values,
        we can iterate through them and add them
        up to make sure that they are lesser than
        the bound value.

        90 / 90 test cases passed.
        Status: Accepted
        Runtime: 56 ms
        """
        """
        # #This would work for any value of bound
        arr_x = []
        arr_y = []

        if x == 1:
            arr_x = [1]
        else:
            i = 0
            while x**i < bound:
                arr_x.append(x**i)
                i += 1

        if y == 1:
            arr_y = [1]
        else:
            j = 0
            while y**j < bound:
                arr_y.append(y**j)
                j += 1
        """

        """
        But, we can observe that 2**18 is larger
        that the bound value, therefore we only
        need to iterate until the number 18
        """
        #         arr_x = [x**i for i in range(18)]
        #         arr_y = [y**j for j in range(18)]

        #         res = set()
        #         for var_x in arr_x:
        #             for var_y in arr_y:
        #                 if (var_x + var_y) <= bound:
        #                     res.add((var_x + var_y))

        #         return list(res)

        # #Code Golf
        return list(set(
            [(var_x + var_y) for var_x in [x ** i for i in range(18)] for var_y in [y ** j for j in range(18)] if
             (var_x + var_y) <= bound]))



