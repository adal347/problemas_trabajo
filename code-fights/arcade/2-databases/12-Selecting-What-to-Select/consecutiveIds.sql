/*Please add ; after each select statement*/
CREATE PROCEDURE consecutiveIds()
BEGIN
    set @count = 0;
	SELECT id AS oldId, (@count := @count + 1) AS newId FROM itemIds;
END