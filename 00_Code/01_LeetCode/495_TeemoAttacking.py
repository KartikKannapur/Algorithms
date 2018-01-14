"""
In LOL world, there is a hero called Teemo and his attacking can
make his enemy Ashe be in poisoned condition. Now, given the
Teemo's attacking ascending time series towards Ashe and the
poisoning time duration per Teemo's attacking, you need to output
the total time that Ashe is in poisoned condition.

You may assume that Teemo attacks at the very beginning of a
specific time point, and makes Ashe be in poisoned condition
immediately.

Example 1:
Input: [1,4], 2
Output: 4
Explanation: At time point 1, Teemo starts attacking Ashe and
makes Ashe be poisoned immediately.
This poisoned status will last 2 seconds until the end of time
point 2.
And at time point 4, Teemo attacks Ashe again, and causes Ashe
to be in poisoned status for another 2 seconds.
So you finally need to output 4.
Example 2:
Input: [1,2], 2
Output: 3
Explanation: At time point 1, Teemo starts attacking Ashe and
makes Ashe be poisoned.
This poisoned status will last 2 seconds until the end of time
point 2.
However, at the beginning of time point 2, Teemo attacks Ashe
again who is already in poisoned status.
Since the poisoned status won't add up together, though the
second poisoning attack will still work at time point 2, it will
stop at the end of time point 3.
So you finally need to output 3.
Note:
You may assume the length of given time series array won't
exceed 10000.
You may assume the numbers in the Teemo's attacking time series
and his poisoning time duration per attacking are non-negative
integers, which won't exceed 10,000,000.

Your runtime beats 25.82 % of python submissions
"""


class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        #Method 1
        if len(timeSeries) == 0:return 0

        arr = [[time, time+duration]for time in timeSeries]
        arr = (sorted(arr, key=lambda ele:ele[0]))

        stack = [arr[0]]

        for elem in arr[1:]:
            stack_top = stack[-1]

            if stack_top[0] <= elem[0] <= stack_top[1]:
                stack_top[1] = min(elem[0], stack_top[1])
                stack.append([max(elem[0], stack_top[1]), elem[1]])

            else:
                stack.append(elem)

        return sum([(i[1] - i[0]) for i in stack])

        # #Method 2:
        n = len(timeSeries)
        total = 0
        for i in range(0, n - 1):
            total += min(duration, timeSeries[i + 1] - timeSeries[i])

        return total + duration if n else 0
