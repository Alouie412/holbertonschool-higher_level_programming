-- This script takes the average temperature of all cities, then lists them in descending order

SELECT city, AVG('value') as avg_temp
FROM temperatures
ORDER BY AVG DESC;
