-- This script displays all tv shows in the passed in database argument
-- This is similar to 10-genre_id_by_show.sql, except we also want to display tv shows with no listed genre
-- As a result, left join is used, as inner join prevents no genre shows from being displayed

SELECT tv_shows.title, tv_show_genres.genre_id
from tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY title, genre_id ASC;
