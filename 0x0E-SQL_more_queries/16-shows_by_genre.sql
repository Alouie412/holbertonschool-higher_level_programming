-- This script displays all tv shows and names of their genres in the passed in database argument
-- This is basically a combination of 11-genre_id_all_shows.sql and multiple join

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name ASC;
