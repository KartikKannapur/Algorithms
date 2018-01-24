/*
Query the sum of Northern Latitudes (LAT_N) from STATION having values greater than  and less than . Truncate your answer to  decimal places.
 */

-- Method 1
SELECT ROUND(SUM(LAT_N), 4) FROM STATION
WHERE LAT_N > 38.7880 AND LAT_N < 137.2345;

-- Method 2
SELECT ROUND(SUM(LAT_N), 4) FROM STATION
WHERE LAT_N BETWEEN 38.7880 AND 137.2345;