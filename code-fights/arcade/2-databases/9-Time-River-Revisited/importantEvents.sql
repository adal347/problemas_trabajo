/*Please add ; after each select statement*/
CREATE PROCEDURE importantEvents()
BEGIN
  SELECT id, name, event_date, participants FROM events
  ORDER BY WEEKDAY(event_date), participants DESC;
END
