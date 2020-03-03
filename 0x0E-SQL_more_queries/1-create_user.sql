-- This script creates the user user_0d_1 and sets their password, if the user
-- does not actually exist. There is another method to do this, but this method
-- does not set any permissions for user_0d_1 (the other one does)
-- The flush command allows enabling changes of the grants table without restarting MYSQL

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
SET PASSWORD FOR 'user_0d_1'@'localhost' = 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
