CREATE PROCEDURE websiteHacking()
    SELECT id,login,name
    FROM users
    WHERE type='user'
    OR type NOT LIKE 'user'
    ORDER BY id
