/*
The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+
Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.

+----------+
| Employee |
+----------+
| Joe      |
+----------+

Your runtime beats 99.91 % of mysql submissions
 */

SELECT E2.Name AS Employee FROM Employee AS E1 JOIN Employee AS E2
ON E1.Id = E2.ManagerId
WHERE E2.Salary > E1.Salary;

SELECT A.name as Employee
FROM Employee A JOIN Employee B
ON A.ManagerId = B.Id
WHERE A.Salary > B.Salary;