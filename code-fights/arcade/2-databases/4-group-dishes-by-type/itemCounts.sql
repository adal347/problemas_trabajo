/*Please add ; after each select statement*/
CREATE PROCEDURE itemCounts()
BEGIN
	SELECT item_name, item_type, COUNT(item_type) AS item_count
  FROM availableItems
  GROUP BY item_type, item_name
  ORDER BY item_type, item_name;
END
