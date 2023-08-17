--  a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT s.name AS name
FROM tv_shows g
LEFT JOIN tv_show_genres gs ON g.id = gs.show_id
LEFT JOIN tv_genres s ON gs.genre_id = s.id
WHERE g.title = 'Dexter'
ORDER BY name ASC;

