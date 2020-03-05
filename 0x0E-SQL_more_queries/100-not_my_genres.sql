-- This script displays the genres not for the show Dexter.
-- This is the exact opposite of 14-my_genres.sql
-- As this script looks for all genres not for Dexter, two select functions are needed

SELECT tv_genres.name
FROM tv_genres
WHERE NOT tv_genres.id IN
    (SELECT tv_genres.id
    FROM tv_genres
    INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name ASC;
