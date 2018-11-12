/*
Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

 */
# -- Method 1 -- Actual Logic
# # SELECT DISTINCT Salary AS SecondHighestSalary FROM Employee
# # ORDER BY SecondHighestSalary DESC
# # LIMIT 1 OFFSET 1;

# -- Logic for LeetCode --
# -- Your runtime beats 98.61 % of mysql submissions --
# SELECT DISTINCT Salary AS SecondHighestSalary FROM Employee
# UNION
# SELECT NULL
# ORDER BY SecondHighestSalary DESC
# LIMIT 1 OFFSET 1


# -- Method 2
# # SELECT MAX(Salary) AS SecondHighestSalary
# # FROM Employee
# # WHERE Salary < (SELECT MAX(Salary) FROM Employee)

# #Method 3

# SELECT IFNULL(A.salary, NULL) AS SecondHighestSalary
# FROM Employee A LEFT JOIN Employee B
# ON A.salary < B.salary
# GROUP BY A.id, A.salary
# HAVING COUNT(DISTINCT B.salary) + 1=2

