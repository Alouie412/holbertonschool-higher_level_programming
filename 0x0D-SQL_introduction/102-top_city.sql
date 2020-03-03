-- This script takes the average temperature of all cities, the lists the top 3 in descending order

SELECT city, AVG('value') AS avg_temp
FROM temperatures
WHERE month = 7 AND month = 8
ORDER BY AVG DESC
LIMIT 3;
