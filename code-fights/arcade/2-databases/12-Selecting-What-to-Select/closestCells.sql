/*Please add ; after each select statement*/
CREATE PROCEDURE closestCells()
BEGIN
     select p.id AS id1,
          (select id
           from positions
           where p.id <> positions.id
           order by power(p.x - positions.x, 2) + power(p.y - positions.y, 2) limit 1
           ) AS id2
        from positions AS p;
END
