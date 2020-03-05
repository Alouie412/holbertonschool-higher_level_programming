-- This script displays all shows whose genre are not considered Comedy.
-- This is the exact opposite of 15-comedy_only.sql, and is similar to 100-not_my_genres.sql

SELECT tv_shows.title
FROM tv_shows
WHERE NOT tv_shows.id IN
    (SELECT tv_shows.id
    FROM tv_shows
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
)
ORDER BY tv_shows.title ASC;
