"""

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
"""


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        """
        Method 1:

        Time Limit Exceeded:15 / 18 test cases passed.
        """
        # self.arr.append(num)

        """
        Method 2:
        Your runtime beats 15.95 % of python3 submissions.
        """
        bisect.insort(self.arr, num)

    def findMedian(self):
        """
        :rtype: float
        """
        index = len(self.arr) // 2
        if len(self.arr) % 2:
            return float(self.arr[index])
        else:
            return (self.arr[index] + self.arr[index - 1]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()