-- Script lists tv shows that have genres listed.

SELECT tv_shows.title AS title, tv_genres.name AS name FROM tv_show_genres JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id RIGHT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id ORDER BY tv_shows.title, name;
