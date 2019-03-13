/*Please add ; after each select statement*/
CREATE PROCEDURE findTable()
BEGIN
    SELECT table_name AS tab_name, column_name AS col_name, data_type
    FROM information_schema.columns
    WHERE table_schema ='ri_db' AND table_name LIKE 'e%s'
    ORDER BY tab_name, col_name;
END