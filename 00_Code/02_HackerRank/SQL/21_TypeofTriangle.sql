/*
Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following statements for each record in the table:

Equilateral: It's a triangle with  sides of equal length.
Isosceles: It's a triangle with  sides of equal length.
Scalene: It's a triangle with  sides of differing lengths.
Not A Triangle: The given values of A, B, and C don't form a triangle.
 */
SELECT IF((A+B)>C AND (A+C)>B AND (B+C)>A ,
          IF(A=B AND A=C AND C=B,'Equilateral',
             IF(A=B OR B=C OR A=C,'Isosceles','Scalene'))
          ,'Not A Triangle') TRIANGLES
FROM TRIANGLES