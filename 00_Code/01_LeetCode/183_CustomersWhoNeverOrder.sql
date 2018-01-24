/*
Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.

Table: Customers.

+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Table: Orders.

+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Using the above tables as example, return the following:

+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
 */

-- Method 1 - Left Join and NULL
-- Your runtime beats 76.22 % of mysql submissions
SELECT Name AS Customers FROM Customers
LEFT JOIN Orders
ON Customers.Id = Orders.CustomerId
WHERE Orders.CustomerId IS NULL;

-- Method 2
-- Your runtime beats 94.63 % of mysql submissions.
SELECT Name AS Customers FROM Customers
WHERE Id NOT IN (SELECT CustomerId from Orders);
