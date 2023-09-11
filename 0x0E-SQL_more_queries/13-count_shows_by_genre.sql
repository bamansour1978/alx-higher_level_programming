-- a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

SELECT
    s.name AS genre,
    COUNT(*) AS number_of_shows
FROM
    tv_genres s
    JOIN tv_show_genres g ON s.id = g.genre_id
GROUP BY
    s.name
ORDER BY
    number_of_shows DESC;
