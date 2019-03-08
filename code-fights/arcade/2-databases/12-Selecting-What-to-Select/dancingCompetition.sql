/*Please add ; after each select statement*/
CREATE PROCEDURE dancingCompetition()
BEGIN
    CREATE OR REPLACE VIEW z(a,b,c,d) AS SELECT * FROM scores;
    SELECT a.*
        FROM scores a, z
        GROUP BY 1
        HAVING (first_criterion  IN (min(b), max(b)))
             + (second_criterion IN (min(c), max(c)))
             + (third_criterion  IN (min(d), max(d))) < 2;
	
END