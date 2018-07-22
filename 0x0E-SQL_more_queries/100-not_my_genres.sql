-- Script lists tv shows that have genres listed.

SELECT DISTINCT tv_genres.name AS name FROM tv_show_genres
INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id WHERE tv_genres.name NOT IN (
     SELECT tv_genres.name FROM tv_show_genres
     INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
     INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
     WHERE tv_shows.title = 'Dexter')
ORDER BY tv_genres.name;
