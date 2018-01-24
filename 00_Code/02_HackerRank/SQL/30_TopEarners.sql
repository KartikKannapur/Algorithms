/*
We define an employee's total earnings to be their monthly  worked, and the maximum total earnings to be the maximum total earnings for any employee in the Employee table. Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings. Then print these values as  space-separated integers.
 */

-- Method 1
SELECT MAX(salary*months) AS maximum_total_earnings, COUNT(*) FROM Employee
WHERE (salary * months) = (SELECT MAX(salary*months) FROM Employee);


-- Method 2
SELECT salary*months AS maximum_total_earnings, COUNT(*) FROM Employee
GROUP BY maximum_total_earnings
ORDER BY maximum_total_earnings DESC
LIMIT 1;