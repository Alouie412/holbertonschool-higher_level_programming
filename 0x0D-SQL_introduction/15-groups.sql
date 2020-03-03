-- This script counts and displays in descending order the score and number of times it appears
-- in the passed in database argument

SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score
ORDER BY score DESC;
