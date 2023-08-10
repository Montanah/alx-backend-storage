--  SQL script that creates a table users with the atributes:
-- id, integer never null, autoincrement, primary key
-- email, string (255 characters), never null, unique
-- name, string (255 characters)

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
