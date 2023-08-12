-- SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
-- Quantity in the table items can be negative.

DELIMITER $$

CREATE TRIGGER update_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Calculate the total quantity to be deducted
    DECLARE total_quantity INT;
    SET total_quantity = NEW.quantity;

    -- Decrease the quantity of the corresponding item
    UPDATE items
    SET quantity = quantity - total_quantity
    WHERE id = NEW.item_id;
END$$

DELIMITER ;