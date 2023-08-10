-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.
-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (you can assume user_id is linked to an existing users)

DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser$$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE average_weighted_score FLOAT;
    DECLARE total_score FLOAT;
    DECLARE total_weight FLOAT;
    DECLARE total_score_weight FLO
    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR
        SELECT score, weight
        FROM projects
        WHERE user_id = user_id;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;
    SET total_score = 0;
    SET total_weight = 0;
    SET total_score_weight = 0;
    read_loop: LOOP
        FETCH cur INTO score, weight;
        IF done THEN
            LEAVE read_loop;
        END IF;
        SET total_score = total_score + score;
        SET total_weight = total_weight + weight;
        SET total_score_weight = total_score_weight + (score * weight);
    END LOOP;
    CLOSE cur;
    SET average_weighted_score = total_score_weight / total_weight;
    INSERT INTO average_score (user_id, score)
    VALUES (user_id, average_weighted_score)
    ON DUPLICATE KEY UPDATE score = average_weighted_score;
END$$

DELIMITER ;