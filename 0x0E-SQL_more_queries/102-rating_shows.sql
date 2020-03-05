-- This script displays the tv shows and their total ratings, grouped by the show title
-- As this script only needed the title name and ratings, only 1 join was needed

SELECT tv_shows.title, SUM(tv_show_ratings.rate) as rating
FROM tv_shows
INNER JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_shows.title
ORDER BY rating DESC;
