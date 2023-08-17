-- a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT c.title, s.genre_id
FROM tv_shows c
JOIN tv_show_genre s ON c.id = s.show_id
ORDER BY c.title, s.genre_id ASC;
