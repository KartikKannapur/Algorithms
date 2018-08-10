"""
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
"""


class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """

        """
        Method 1:

        * Convert the string 'HH:MM' into integer in terms of minutes
        * Sort the integers in ascending order
        * Append the first element in the array to the last to take care
        of rollover time stamp
        * Calculate differences between successive elements
        * Return the minimum value

        Your runtime beats 82.07 % of python3 submissions.
        """

        # #Convert the string 'HH:MM' into integer in terms of minutes
        arrTimePoints = []
        for ele in timePoints:
            hh, mm = ele.split(':')
            arrTimePoints.append((int(hh) * 60) + (int(mm)))

        # #Sort the integers in ascending order
        arrTimePoints.sort()

        # #Append the first element in the array to the last to take care
        # #of rollover time stamp
        arrTimePoints.append(arrTimePoints[0] + (24 * 60))

        # #Calculate differences between successive elements
        arrTimePointsDiff = []
        for index in range(1, len(arrTimePoints)):
            arrTimePointsDiff.append(arrTimePoints[index] - arrTimePoints[index - 1])

        # #Return the minimum value
        return min(arrTimePointsDiff)