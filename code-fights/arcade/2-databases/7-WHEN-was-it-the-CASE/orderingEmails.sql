/*Please add ; after each select statement*/
CREATE PROCEDURE orderingEmails()
BEGIN
	SELECT id, email_title,
          if(size >> 20 > 0,
             CONCAT_WS(' ', size >> 20, 'Mb'),
             CONCAT_WS(' ', size >> 10, 'Kb')
            ) AS short_size
    FROM emails
    ORDER BY size DESC;
END
