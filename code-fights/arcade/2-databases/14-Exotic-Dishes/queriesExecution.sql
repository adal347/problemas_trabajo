/*Please add ; after each select statement*/
CREATE PROCEDURE queriesExecution()
BEGIN
    set @tbl = concat(
        (select group_concat(
            concat('select "', query_name, '" query_name, (', code, ') val') separator ' union ') 
        from queries), ' order by 1');

    prepare qry from @tbl;
    execute qry;
END