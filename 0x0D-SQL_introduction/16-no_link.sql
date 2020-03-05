-- This script displays all names in descending order by score in the passed in database argument
-- Note: any records without the name value will not be printed out

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
