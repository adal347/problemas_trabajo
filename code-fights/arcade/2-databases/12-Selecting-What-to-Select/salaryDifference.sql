/*Please add ; after each select statement*/
CREATE PROCEDURE salaryDifference()
BEGIN
	SET @maxSalary = (SELECT MAX(salary) FROM employees);
	SET @minSalary = (SELECT MIN(salary) FROM employees);
	SET @countMaxSalary = (SELECT COUNT(salary) FROM employees WHERE salary = @maxSalary);
	SET @countMinSalary = (SELECT COUNT(salary) FROM employees WHERE salary = @minSalary);
    SELECT IFNULL((@maxSalary * @countMaxSalary) - (@minSalary * @countMinSalary), 0) AS difference;
END