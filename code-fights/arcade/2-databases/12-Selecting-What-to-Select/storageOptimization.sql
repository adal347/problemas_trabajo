/*Please add ; after each select statement*/
CREATE PROCEDURE storageOptimization()
BEGIN
	SELECT id, 
           ELT(x, "name", "date_of_birth", "salary") column_name, 
           ELT(x, name, date_of_birth, salary) value 
        FROM workers_info,
             (SELECT 1 x UNION SELECT 2 UNION SELECT 3) a
        HAVING value IS NOT NULL
        ORDER BY 1, x;
END