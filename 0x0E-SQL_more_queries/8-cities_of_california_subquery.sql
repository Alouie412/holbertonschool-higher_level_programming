-- This script lists all cities of California that are in the passed in database argument
-- Usage of subquery is necessary

SELECT id, name
FROM cities
WHERE state_id =
    (SELECT id
    FROM states
    WHERE name = 'California');
