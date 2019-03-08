/*Please add ; after each select statement*/
CREATE PROCEDURE checkExpenditure()
BEGIN
	SELECT id, -LEAST(0, value - sum(expenditure_sum)) loss
    FROM
        expenditure_plan,
        allowable_expenditure
    WHERE WEEK(monday_date) BETWEEN left_bound AND right_bound
    GROUP BY 1;
END