-- This script takes the average temperature of all cities only within a certain month timeframe,
-- then lists the top three in descending order

SELECT city, AVG(temperatures.value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
