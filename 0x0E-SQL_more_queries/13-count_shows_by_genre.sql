-- This script displays the genre name and number of shows that fall under each genre
-- Shows without genres are ignored

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
from tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
