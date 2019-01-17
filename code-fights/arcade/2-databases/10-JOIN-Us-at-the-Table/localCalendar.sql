/*Please add ; after each select statement*/
CREATE PROCEDURE localCalendar()
BEGIN
	SELECT event_id,
            DATE_FORMAT(DATE_ADD(date, INTERVAL timeshift minute),
                                IF(hours = 24, "%Y-%m-%d %H:%i", "%Y-%m-%d %h:%i %p")) AS formatted_date
    FROM events INNER JOIN settings ON events.user_id = settings.user_id;
END
