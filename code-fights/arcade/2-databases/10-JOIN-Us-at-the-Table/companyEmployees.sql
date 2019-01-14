/*Please add ; after each select statement*/
CREATE PROCEDURE companyEmployees()
BEGIN
	SELECT dep_name, emp_name FROM departments FULL JOIN employees
    ORDER BY dep_name, emp_name;
END
