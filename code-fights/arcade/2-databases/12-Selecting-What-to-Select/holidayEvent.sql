/*Please add ; after each select statement*/
CREATE PROCEDURE holidayEvent()
BEGIN
    set @count = 0;
    SELECT buyer_name AS winners
    FROM (SELECT (@count := @count + 1) AS id, buyer_name FROM purchases) as p
    WHERE MOD(id, 4) = 0
    GROUP BY winners;
END