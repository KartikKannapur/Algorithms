"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.


"""


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        """
        Method 1: Array

        * Initially set buy to the first index & traverse
        through the array
        * IF the next index is smaller than `buy`, update `buy`
        * At each index, compare the buy with the current index
        i.e. the sell index
        * At each index, update the max variable

        Your runtime beats 41.97 % of python3 submissions.
        """

        if not prices:
            return 0

        buy = prices[0]
        sell = prices[0]
        res = 0

        for ele in prices:
            # #Update buy to the minimum value each time
            buy = min(ele, buy)

            # #Update the sell value each time, as the
            # #current value i.e. ele minus the buy value
            sell = ele - buy

            # #Update the result each time
            res = max(sell, res)

        return res


