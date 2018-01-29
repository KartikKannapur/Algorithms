"""
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
"""

import itertools
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        hours = [8, 4, 2, 1]
        minutes = [32, 16, 8, 4, 2, 1]

        def get_time(time, n, limit):
            ans = []
            for comb in itertools.combinations(time, n):
                tmp = sum(comb)
                if tmp < limit:
                    ans.append(tmp)
            return ans

        ans = []
        for i in range(0, num + 1):
            for _h in get_time(hours, i, 12):
                for _m in get_time(minutes, num - i, 60):
                    ans.append('{:}:{:02}'.format(_h, _m))
        return ans

