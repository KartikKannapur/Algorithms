"""
Write a SQL query to find all numbers that appear at least three times consecutively.

+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+
For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.

+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
"""

SELECT DISTINCT A.Num AS "ConsecutiveNums" FROM logs A JOIN logs B
ON (A.id+1 = B.id) AND (A.Num = B.Num) JOIN logs C
ON (B.id+1 = C.id) AND (B.Num = C.Num)