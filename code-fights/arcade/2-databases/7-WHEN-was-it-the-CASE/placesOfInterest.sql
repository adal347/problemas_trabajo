/*Please add ; after each select statement*/
CREATE PROCEDURE placesOfInterest()
BEGIN
	SELECT country,
    SUM((leisure_activity_type = "Adventure park") * number_of_places) AS adventure_park,
    SUM((leisure_activity_type = "Golf") * number_of_places) AS golf,
    SUM((leisure_activity_type = "River cruise") * number_of_places) AS river_cruise,
    SUM((leisure_activity_type = "Kart racing") * number_of_places) AS kart_racing
  FROM countryActivities
  GROUP BY country;
END
