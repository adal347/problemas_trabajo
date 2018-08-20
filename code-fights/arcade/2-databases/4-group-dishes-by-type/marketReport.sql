/*Please add ; after each select statement*/
CREATE PROCEDURE marketReport()
BEGIN
  SELECT country, COUNT(country) AS competitors FROM foreignCompetitors
  GROUP BY country
  UNION
  SELECT 'Total:', COUNT(*) FROM foreignCompetitors;
END
