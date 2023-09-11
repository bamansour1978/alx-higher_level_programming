-- a script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT g.title AS title
FROM tv_shows g
JOIN tv_show_genres gs ON g.id = gs.show_id
JOIN tv_genres s ON gs.genre_id = s.id
WHERE s.name = 'Comedy'
ORDER BY title ASC;
