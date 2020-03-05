-- This script prints out the highest recorded temperature for each state in descending order

SELECT state, MAX(temperatures.value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;
