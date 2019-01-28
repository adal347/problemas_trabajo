/*Please add ; after each select statement*/
CREATE PROCEDURE sunnyHolidays()
BEGIN
	SELECT holiday_date AS ski_date FROM holidays
    WHERE EXISTS (
        SELECT 1 FROM weather WHERE sunny_date = holiday_date
    )
    ORDER BY ski_date;
END
