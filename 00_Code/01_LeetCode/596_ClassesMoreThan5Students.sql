/*
There is a table courses with columns: student and class

Please list out all classes which have more than or equal to 5 students.

For example, the table:

+---------+------------+
| student | class      |
+---------+------------+
| A       | Math       |
| B       | English    |
| C       | Math       |
| D       | Biology    |
| E       | Math       |
| F       | Computer   |
| G       | Math       |
| H       | Math       |
| I       | Math       |
+---------+------------+
Should output:

+---------+
| class   |
+---------+
| Math    |
+---------+
Note:
The students should not be counted duplicate in each course.

*/


# #Your runtime beats 70.77 % of mysql submissions.
# SELECT class
# FROM (
#     SELECT DISTINCT student, class
#     FROM courses
# ) As t
# GROUP BY class
# HAVING COUNT(*) >= 5;


SELECT
    class
FROM
    courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5;