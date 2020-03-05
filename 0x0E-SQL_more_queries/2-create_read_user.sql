-- This script creates the user user_0d_2, sets the password, and gives select privileges to the newly created
-- database hbtn_0d_2
-- Using IDENTIFIED BY is another option for creating user and setting password

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
SET PASSWORD FOR 'user_0d_2'@'localhost' = 'user_0d_2_pwd';
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
