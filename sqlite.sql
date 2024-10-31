-- Active: 1730210512993@@127.0.0.1@3306
SELECT * FROM users;

INSERT INTO users (id, username, email, hashed_password, is_active, is_admin) 
    VALUES (1, 'administrator', 'admin@exemple.com', '1234', TRUE, TRUE);

DELETE FROM users WHERE id = 1;
