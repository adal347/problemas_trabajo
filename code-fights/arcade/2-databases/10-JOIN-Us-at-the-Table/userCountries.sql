/*Please add ; after each select statement*/
CREATE PROCEDURE userCountries()
BEGIN
	SELECT id, IFNULL(country, "unknown") AS country
    FROM users LEFT OUTER JOIN cities
    ON users.city = cities.city
    ORDER BY id;
END
