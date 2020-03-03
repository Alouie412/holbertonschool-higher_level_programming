-- This script prints out all scores and names, in descending order
-- set by the condition in the passed in database argument

SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
