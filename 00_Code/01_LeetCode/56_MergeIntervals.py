"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

Your runtime beats 74.99 % of python submissions.
"""


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0: return []

        intervals = sorted(intervals, key=lambda ele: ele.start)

        stack = [(intervals[0])]

        for elem in intervals[1:]:
            stack_top = stack[-1]

            if stack_top.start <= elem.start <= stack_top.end:
                stack_top.end = max(elem.end, stack_top.end)
            else:
                stack.append(elem)

        return stack

