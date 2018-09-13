/*Please add ; after each select statement*/
CREATE PROCEDURE newsSubscribers()
BEGIN

  SELECT subscriber FROM full_year
  WHERE newspaper LIKE '%Daily%'
  UNION
  SELECT subscriber FROM half_year
  WHERE newspaper LIKE '%Daily%'
  GROUP BY subscriber
  ORDER BY subscriber;
END