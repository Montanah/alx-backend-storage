--  SQL script that creates a function SafeDiv that divides (and returns) the
-- first by the second number or returns 0 if the second number is equal to 0.
-- -- Function SafeDiv is taking 2 inputs (in this order):
-- -- a, a number
-- -- b, a number
-- And returns a / b or 0 if b == 0

DELIMITER $$

DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv(
    a INT,
    b INT
    )
    RETURNS INT
    DETERMINISTIC
    BEGIN
        IF b = 0 THEN
            RETURN 0;
        ELSE
            RETURN a / b;
        END IF;
    END$$

DELIMITER ;