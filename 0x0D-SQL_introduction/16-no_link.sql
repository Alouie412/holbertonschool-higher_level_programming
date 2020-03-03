-- This script displays all names in descending order by score in the passed in database argument
-- Note: any records without the name value will not be printed out

SELECT score, name
FROM second_table
WHERE EXISTS
(SELECT name FROM second_table)
ORDER BY score DESC;
