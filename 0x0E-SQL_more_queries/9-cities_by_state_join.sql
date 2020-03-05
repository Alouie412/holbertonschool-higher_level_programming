-- This script displays all cities in the passed in database argument
-- Using inner join, this script takes the table in both cities and states, returns a match in both
-- tables, and displays the cities.id, cities.name, and states.name

SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities ON cities.state_id = states.id
