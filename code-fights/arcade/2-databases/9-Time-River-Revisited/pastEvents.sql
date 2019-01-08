/*Please add ; after each select statement*/
CREATE PROCEDURE pastEvents()
BEGIN
	SELECT name, event_date FROM Events
    WHERE event_date < (SELECT MAX(event_date) FROM Events)
            AND event_date >= DATE_SUB((SELECT MAX(event_date) FROM Events), INTERVAL 1 WEEK)
    ORDER BY event_date DESC;
END
