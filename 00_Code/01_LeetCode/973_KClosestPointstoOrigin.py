"""
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)



Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)


Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""

import math


class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        #         """
        #         Method 1: Hash Map + Sorting
        #         * Compute the Euclidean distance between each point
        #         and the origin
        #         * Store the distance and the point in a hash map
        #         * Sort the hash map by distance and return the values

        #         Complexity: O(n) + O(nlogn) + O(n) = O(nlogn)
        #         Your runtime beats 21.98 % of python3 submissions.
        #         """

        #         def euclidean_distance(x):
        #             return math.sqrt((x[0])**2 + (x[1])**2)

        #         d = {} # #{distance: [points]}

        #         for ele in points:
        #             var_dist = euclidean_distance(ele)
        #             if var_dist in d:
        #                 d[var_dist].append(ele)
        #             else:
        #                 d[var_dist] = [ele]

        #         d_sorted = sorted(d.items(), key=lambda ele:ele[0])

        #         res = []
        #         return [ele for k,v in d_sorted for ele in v][:K]

        """
        Method 2: Same logic as Method 1
        Written more effeciently

        Complexity: O(nlogn)
        Your runtime beats 78.67 % of python3 submissions.
        """
        points.sort(key=lambda ele: ele[0] ** 2 + ele[1] ** 2)
        return points[:K]

        """
        Method 3: Heap

        Your runtime beats 44.90 % of python3 submissions.
        """
        # return heapq.nsmallest(K, points, lambda ele: ele[0]**2 + ele[1]**2)