/*Please add ; after each select statement*/
CREATE PROCEDURE netIncome()
BEGIN
	SELECT year(date) AS year, quarter(date) AS quarter,
          SUM(profit) - SUM(loss) AS net_profit
  FROM accounting
  GROUP BY 1, 2;
END
