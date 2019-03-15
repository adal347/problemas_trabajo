/*Please add ; after each select statement*/
CREATE PROCEDURE bugsInComponent()
BEGIN
    SELECT Bug.title AS bug_title,
           Component.title AS component_title,
           (SELECT SUM(1) FROM BugComponent WHERE component_id = id) AS bugs_in_component
        FROM Bug INNER JOIN BugComponent ON bug_num=num
        INNER JOIN Component ON component_id = id
        WHERE (SELECT SUM(1) FROM BugComponent WHERE bug_num = num) > 1
        ORDER BY bugs_in_component DESC, id, num;
END