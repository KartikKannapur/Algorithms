/*
Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.

Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

Input Format

The CITY and COUNTRY tables are described as follows: CITY.jpg

Country.jpg
 */
SELECT A.NAME FROM
CITY A JOIN COUNTRY B ON A.COUNTRYCODE = B.CODE
WHERE B.CONTINENT = 'Africa'