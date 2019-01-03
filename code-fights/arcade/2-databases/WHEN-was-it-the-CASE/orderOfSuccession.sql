/*Please add ; after each select statement*/
CREATE PROCEDURE orderOfSuccession()
BEGIN
	SELECT
    CASE
        WHEN gender = "F" THEN CONCAT("Queen ", name)
        ELSE CONCAT("King ", name)
    END AS name
    FROM Successors ORDER BY birthday;
END
