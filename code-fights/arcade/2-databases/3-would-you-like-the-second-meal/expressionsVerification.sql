/*Please add ; after each select statement*/
CREATE PROCEDURE expressionsVerification()
BEGIN
  SELECT * FROM expressions
  WHERE c LIKE
    CASE operation
      WHEN '+' THEN a + b
      WHEN '-' THEN a - b
      WHEN '*' THEN a * b
      ELSE IF (a % b = 0, FORMAT(a / b, 0), a / b)
    END;
END
