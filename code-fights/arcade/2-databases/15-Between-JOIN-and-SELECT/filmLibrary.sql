/*Please add ; after each select statement*/
CREATE PROCEDURE filmLibrary()
BEGIN
    SET @genre = (SELECT genre
    FROM movies
    GROUP BY genre
    ORDER BY COUNT(1) DESC
    LIMIT 1);
	SELECT aa.actor, age FROM actor_ages AS aa 
    INNER JOIN starring_actors AS sa ON aa.actor = sa.actor
    INNER JOIN movies ON movie = movie_name
    WHERE genre = @genre
    ORDER BY age DESC, aa.actor;
END