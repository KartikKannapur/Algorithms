"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:
Input:
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation:
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
Example 2:
Input:
asteroids = [8, -8]
Output: []
Explanation:
The 8 and -8 collide exploding each other.
Example 3:
Input:
asteroids = [10, 2, -5]
Output: [10]
Explanation:
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.
Example 4:
Input:
asteroids = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
Explanation:
The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each other.
Note:

The length of asteroids will be at most 10000.
Each asteroid will be a non-zero integer in the range [-1000, 1000]..
"""


class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        """
        Method 1: Stack

        1. IF the stack is empty or the asteroid is positive, push to stack
        2. IF the asteroid is negative AND stack exists AND stack top is positive
        - equal to magnitude of stack top --> destroy both
        - stack top is smaller --> pop stack top
        - stack top is larger --> do nothing

        3. IF the asteroid is negative AND stack top is also negative
        - push asteroid to stack

        Your runtime beats 91.05 % of python submissions.
        """
        res = []

        for asteroid in asteroids:
            if len(res) == 0 or asteroid > 0:
                res.append(asteroid)

            elif asteroid < 0:
                # #while top of the stack is positive.
                while res and res[-1] > 0:
                    # Both asteroids are equal, destroy both.
                    if res[-1] == -asteroid:
                        res.pop()
                        break

                    # Stack top is smaller, remove the +ve asteroid
                    # from the stack and continue the comparison.
                    elif res[-1] < -asteroid:
                        res.pop()
                        continue

                    # Stack top is larger, -ve asteroid is destroyed.
                    elif res[-1] > -asteroid:
                        break
                else:
                    # -ve asteroid made it all the way to the
                    # bottom of the stack and destroyed all asteroids.
                    res.append(asteroid)
        return res