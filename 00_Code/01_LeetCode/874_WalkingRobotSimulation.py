"""
A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three possible types of commands:

-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units
Some of the grid squares are obstacles.

The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will be from the origin.



Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)
Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)
"""


class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """

        """
        Method 1:

        """
        x, y, direction = 0, 0, 0
        max_dist = 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        dict_x = {}
        dict_y = {}

        for obstacle in obstacles:
            if obstacle[0] not in dict_x:
                dict_x[obstacle[0]] = [obstacle[1]]
            else:
                dict_x[obstacle[0]].append(obstacle[1])
            if obstacle[1] not in dict_y:
                dict_y[obstacle[1]] = [obstacle[0]]
            else:
                dict_y[obstacle[1]].append(obstacle[0])

        # direction 0: north, 1: east, 2: south, 3: west
        for command in commands:
            if command == -1:
                direction = (direction + 1) % 4
            elif command == -2:
                direction = (direction - 1) % 4

            else:
                if (direction == 0 or direction == 2) and x not in dict_x:
                    y += dy[direction] * command
                elif (direction == 1 or direction == 3) and y not in dict_y:
                    x += dx[direction] * command
                else:
                    while command:
                        if (direction == 0 or direction == 2) and y + dy[direction] not in dict_x[x]:
                            y = y + dy[direction]
                        elif (direction == 1 or direction == 3) and x + dx[direction] not in dict_y[y]:
                            x = x + dx[direction]
                        command -= 1
                if x ** 2 + y ** 2 > max_dist: max_dist = x ** 2 + y ** 2
        return max_dist