/*Please add ; after each select statement*/
CREATE PROCEDURE emptyDepartments()
BEGIN
	SELECT dep_name FROM departments WHERE NOT EXISTS (
        SELECT 1 FROM employees WHERE department = departments.id
    )
    ORDER BY id;
END
