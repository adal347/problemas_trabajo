/*Please add ; after each select statement*/
CREATE PROCEDURE recentHires()
BEGIN
    SELECT name AS names 
        FROM ((SELECT 1 department, name FROM pr_department ORDER BY date_joined DESC LIMIT 5)
              UNION ALL
              (SELECT 2, name FROM it_department ORDER BY date_joined DESC LIMIT 5)
              UNION ALL
              (SELECT 3, name FROM sales_department ORDER BY date_joined DESC LIMIT 5)
             ) AS names_department 
        ORDER BY department, name; 
END