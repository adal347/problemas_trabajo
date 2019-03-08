/*Please add ; after each select statement*/
CREATE PROCEDURE trackingSystem()
BEGIN
	SELECT distinct anonymous_id as anonym_id,
        (SELECT event_name FROM tracks AS b WHERE b.anonymous_id = a.anonymous_id AND b.user_id IS NULL ORDER BY received_at DESC LIMIT 1) as last_null,
        (SELECT event_name FROM tracks AS b WHERE b.anonymous_id = a.anonymous_id AND b.user_id IS NOT NULL ORDER BY received_at ASC LIMIT 1) as first_notnull
    FROM tracks AS a ORDER BY a.anonymous_id;
END