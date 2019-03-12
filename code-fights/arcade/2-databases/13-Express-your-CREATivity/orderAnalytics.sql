DROP PROCEDURE IF EXISTS orderAnalytics;
CREATE PROCEDURE orderAnalytics()
BEGIN

    DROP TABLE IF EXISTS order_analytics;
    CREATE TABLE order_analytics (
        id INT NOT NULL PRIMARY KEY,
        year VARCHAR(4),
        quarter TINYINT,
        type VARCHAR(10),
        total_price INT
    );

    INSERT INTO order_analytics (id, year, quarter, type, total_price)
    SELECT id, YEAR(order_date) as year, QUARTER(order_date) AS quarter,
            type, (quantity * price) AS total
    FROM orders;

    SELECT *
    FROM order_analytics
    ORDER by id;
END;
