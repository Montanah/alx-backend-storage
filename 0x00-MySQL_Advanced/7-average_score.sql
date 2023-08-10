-- SQL script that creates a stored procedure ComputeAverageScoreForUser that
-- computes and store the average score for a student. Note: An average score
-- can be a decimal
-- Procedure ComputeAverageScoreForUser is taking 1 input (in this order):
-- user_id, a users.id value (you can assume user_id is linked to an existing users)

DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
    )

BEGIN
    
        DECLARE average_score DECIMAL(10,2);
    
        SELECT AVG(score) INTO average_score
        FROM scores
        WHERE user_id = user_id;
    
        INSERT INTO average_scores (user_id, average_score)
        VALUES (user_id, average_score);
    
    END$$

DELIMITER ;