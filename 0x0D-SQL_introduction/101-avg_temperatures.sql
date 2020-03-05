-- This script takes the average temperature of all cities, then lists them in descending order

SELECT city, AVG(temperatures.value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
